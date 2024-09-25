import time


class Message:
    def __init__(self, content, level, namespace, timestamp_format):
        self.content = content
        self.level = level
        self.namespace = namespace
        self.timestamp = time.strftime(timestamp_format)