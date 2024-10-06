import os
import shutil
from datetime import datetime

def backup_directory(source_dir, backup_dir):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    destination = os.path.join(backup_dir, f"backup_{timestamp}")
    shutil.copytree(source_dir, destination)
    print(f"Backup created at {destination}")

if __name__ == "__main__":
    source_dir = "/path/to/source"
    backup_dir = "/path/to/backup"
    backup_directory(source_dir, backup_dir)
