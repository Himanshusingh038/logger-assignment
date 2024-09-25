import threading
from concurrent.futures import ThreadPoolExecutor
from src.log.enum import ThreadModel, WriteMode
from src.log.logger_config import LoggerConfig
from src.log.message import Message

class Logger:
    _instance = None  # Class variable to hold the singleton instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self, config: LoggerConfig):
        if not hasattr(self, 'initialized'):  # Prevent re-initialization
            self.config = config
            # Create a thread pool for asynchronous logging if thread model is multi-thread
            self.executor = ThreadPoolExecutor() if self.config.thread_model == ThreadModel.MULTI else None
            self.initialized = True  # Set to True to mark initialization as complete

    def log(self, content, level, namespace):
        if level.value >= self.config.log_level.value:
            message = Message(content, level, namespace, self.config.timestamp_format)
            if self.config.thread_model == ThreadModel.SINGLE:
                # Log in the same thread
                self._write_message(message)
            else:
                # Log in a separate thread
                self.executor.submit(self._write_message, message)

    def _write_message(self, message):
        if self.config.write_mode == WriteMode.SYNC:
            for sink in self.config.sinks:
                if sink.level.value <= message.level.value:
                    sink.write(message)
        else:  # ASYNC mode
            if self.config.thread_model == ThreadModel.SINGLE:
                # Run the write operation in a separate thread if using async write mode
                threading.Thread(target=self._async_write_message, args=(message,)).start()
            else:
                # Use the thread pool if using multi-threaded logging
                self.executor.submit(self._async_write_message, message)

    def _async_write_message(self, message):
        for sink in self.config.sinks:
            if sink.level.value <= message.level.value:
                sink.write(message)
