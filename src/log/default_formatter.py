from src.log.formatter import LogFormatter
from src.log.message import Message


class DefaultLogFormatter(LogFormatter):
    """Default implementation of a log formatter."""
    
    def format(self, message: Message) -> str:
        return f"{message.level.name} [{message.timestamp}] {message.namespace}: {message.content}"