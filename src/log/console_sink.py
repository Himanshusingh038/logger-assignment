from src.log.default_formatter import DefaultLogFormatter
from src.log.message import Message
from src.log.sink import Sink

class ConsoleSink(Sink):
    
    def __init__(self, level, formatter=None):
        super().__init__(level)
        self.formatter = formatter or DefaultLogFormatter()  # Use provided formatter or default

    def write(self, message: Message):
        """Write a message to the console."""
        log_msg = self.formatter.format(message)
        print(log_msg)
