from datetime import datetime

class Logger:
    def __init__(self, log_path="backup_log.txt"):
        self.log_path = log_path

    def log(self, message):
        with open(self.log_path, "a") as log_file:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_file.write(f"[{timestamp}] {message}\n")