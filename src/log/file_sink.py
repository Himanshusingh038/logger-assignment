import gzip
import os

from fastapi import HTTPException

from src.log.default_formatter import DefaultLogFormatter
from src.log.message import Message

formatter_obj = DefaultLogFormatter()

class FileSink:
    def __init__(self, level, file_path, max_size_kb=100, backup_count=3):
        self.level = level
        self.file_path = file_path
        self.max_size_kb = max_size_kb
        self.backup_count = backup_count
        self.current_file_size = self._get_file_size()
        self.formatter = formatter_obj
        self._cleanup_old_logs()


    def _get_file_size(self):
        """Recalculate the file size in kilobytes."""
        if os.path.exists(self.file_path):
            return os.path.getsize(self.file_path) // 1024
        return 0
    
    def _cleanup_old_logs(self):
        """Remove old log files based on the backup count."""
        i=self.backup_count+1
        while os.path.exists(f"{self.file_path}.{i}.gz"):
            os.remove(f"{self.file_path}.{i}.gz")
            i+=1

    def _rotate_logs(self):
        """Rotate and compress logs when the file exceeds max_size_kb."""
        print(f"file {self.file_path} size is {self._get_file_size()}kb")
        try:
            if os.path.exists(self.file_path):
                print(f"Rotating logs for {self.file_path}")

                # Rotate existing log files, moving backup files up incrementally
                for i in range(self.backup_count - 1, 0, -1):
                    old_file = f"{self.file_path}.{i}.gz"
                    new_file = f"{self.file_path}.{i + 1}.gz"

                    if os.path.exists(new_file):
                        os.remove(new_file)  # Remove the existing new file before renaming
                    if os.path.exists(old_file):
                        os.rename(old_file, new_file)
                
                # Rename the current log to .1 before compression
                os.rename(self.file_path, f"{self.file_path}.1")

                # Compress the most recent log file (app.log.1)
                with open(f"{self.file_path}.1", 'rb') as f_in:
                    with gzip.open(f"{self.file_path}.1.gz", 'wb') as f_compressed:
                        f_compressed.writelines(f_in)

                # Remove the uncompressed version after compression
                os.remove(f"{self.file_path}.1")

            else:
                print(f"Log file {self.file_path} not found for rotation")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred : {str(e)}")

    def write(self, message: Message):
        """Write a message to the log file, rotate logs if necessary."""
        try:
            log_msg = self.formatter.format(message) + '\n'
            log_msg_size_kb = len(log_msg.encode('utf-8')) // 1024

            # Recalculate the file size after each write operation
            self.current_file_size = self._get_file_size()
            # print(f'file size {self.current_file_size}')
            if self.current_file_size + log_msg_size_kb >= self.max_size_kb:
                self._rotate_logs()
                self.current_file_size = 0  # Reset the size after rotation

            # Append the log message to the file
            with open(self.file_path, 'a') as f:
                f.write(log_msg)
                self.current_file_size += log_msg_size_kb
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred : {str(e)}")
