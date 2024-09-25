from src.enum.log_level import LogLevel
from src.log.enum import ThreadModel, WriteMode


class LoggerConfig:
    def __init__(self, timestamp_format="%Y-%m-%d %H:%M:%S", log_level=LogLevel.INFO, sinks=None,
                 thread_model=ThreadModel.SINGLE, write_mode=WriteMode.SYNC):
        self.timestamp_format = timestamp_format
        self.log_level = log_level
        self.sinks = sinks or []
        self.thread_model = thread_model
        self.write_mode = write_mode