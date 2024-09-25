from enum import Enum


class ThreadModel(Enum):
    SINGLE = "SINGLE"
    MULTI = "MULTI"

class WriteMode(Enum):
    SYNC = "SYNC"
    ASYNC = "ASYNC"
