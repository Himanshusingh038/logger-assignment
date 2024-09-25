from abc import ABC, abstractmethod
from src.log.message import Message

class LogFormatter(ABC):
    """Abstract base class for log formatters."""
    
    @abstractmethod
    def format(self, message: Message) -> str:
        """Format the log message."""
        pass
