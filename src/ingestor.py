import time
import os

class LogIngestor:
    def __init__(self, file_path):
        self.file_path = file_path

    def follow(self):
        """Generator that yields new lines from the log file."""
        if not os.path.exists(self.file_path):
             # Wait for file to be created
             while not os.path.exists(self.file_path):
                 time.sleep(1)

        with open(self.file_path, 'r') as f:
            # Go to the end of the file
            f.seek(0, 2)
            
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                yield line.strip()
