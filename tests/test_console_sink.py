import unittest
from unittest.mock import MagicMock
from src.enum.log_level import LogLevel
from src.log.message import Message
from src.log.console_sink import ConsoleSink

class TestConsoleSink(unittest.TestCase):
    def test_write_message(self):
        # Arrange
        mock_formatter = MagicMock()
        mock_formatter.format.return_value = "INFO [2023-09-25 10:00:00] namespace: Test message"
        console_sink = ConsoleSink(level=LogLevel.INFO, formatter=mock_formatter)
        message = Message("Test message", LogLevel.INFO, "namespace", "%Y-%m-%d %H:%M:%S")

        # Act
        with unittest.mock.patch('builtins.print') as mock_print:
            console_sink.write(message)

        # Assert
        mock_print.assert_called_once_with("INFO [2023-09-25 10:00:00] namespace: Test message")
        mock_formatter.format.assert_called_once_with(message)

if __name__ == '__main__':
    unittest.main()