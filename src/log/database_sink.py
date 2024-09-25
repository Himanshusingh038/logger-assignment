import sqlite3
from src.log.sink import Sink
from src.log.message import Message

class DatabaseSink(Sink):
    def __init__(self, level, db_path="logs.db"):
        super().__init__(level)
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self):
        """Create the logs table if it doesn't exist."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                level TEXT,
                namespace TEXT,
                content TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def write(self, message: Message):
        """Write a message to the SQLite database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        log_entry = (message.timestamp, message.level.name, message.namespace, message.content)
        cursor.execute('''
            INSERT INTO logs (timestamp, level, namespace, content)
            VALUES (?, ?, ?, ?)
        ''', log_entry)

        conn.commit()
        conn.close()
