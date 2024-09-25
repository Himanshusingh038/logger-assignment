from abc import ABC, abstractmethod
from src.log.message import Message

class Sink(ABC):
    def __init__(self, level):
        self.level = level

    @abstractmethod
    def write(self, message: Message):
        pass