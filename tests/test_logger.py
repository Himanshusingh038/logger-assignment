import unittest
from src.enum.log_level import LogLevel
from src.log.logger import Logger
from src.log.logger_config import LoggerConfig
from src.log.file_sink import FileSink
from src.log.enum import ThreadModel, WriteMode
import os

class TestLogger(unittest.TestCase):

    def setUp(self):
        # Set up the logger configuration for testing
        self.logger_config = LoggerConfig(
            timestamp_format="%d-%m-%Y %H:%M:%S",
            log_level=LogLevel.DEBUG,
            sinks=[FileSink(level=LogLevel.DEBUG, file_path="test_log.log", max_size_kb=50)],
            thread_model=ThreadModel.SINGLE,  # Use SINGLE for simplicity in tests
            write_mode=WriteMode.SYNC           # Use SYNC for immediate writing
        )
        self.logger = Logger(self.logger_config)

    def tearDown(self):
        # Clean up after each test (remove log files, etc.)
        if os.path.exists("test_log.log"):
            os.remove("test_log.log")

    def test_log_debug_message(self):
        # Test logging a DEBUG level message
        self.logger.log("This is a debug message", level=LogLevel.DEBUG, namespace="TestNamespace")
        with open("test_log.log", "r") as f:
            log_content = f.read()
        self.assertIn("DEBUG", log_content)
        self.assertIn("This is a debug message", log_content)

    def test_log_info_message(self):
        # Test logging an INFO level message
        self.logger.log("This is an info message", level=LogLevel.INFO, namespace="TestNamespace")
        with open("test_log.log", "r") as f:
            log_content = f.read()
        self.assertIn("INFO", log_content)
        self.assertIn("This is an info message", log_content)

if __name__ == '__main__':
    unittest.main()
