import os
import shutil
import schedule
import time
from datetime import datetime

def perform_backup(source_path, destination_directory):
    if not os.path.isfile(source_path):
        print(f"Source file not found: {source_path}")
        return

    os.makedirs(destination_directory, exist_ok=True)

    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    source_name = os.path.basename(source_path)
    name, extension = os.path.splitext(source_name)

    backup_filename = f"{name}_{timestamp}{extension}"
    destination_path = os.path.join(destination_directory, backup_filename)

    # Copy the source file to the destination directory.
    shutil.copy2(source_path, destination_path)

    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    with open("backup_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(
            f"Backup completed successfully at {current_time}\n"
            f"Source: {source_path}\n"
            f"Backup: {destination_path}\n\n"
        )

    print(f"Backup completed successfully at {current_time}")
    print(f"Backup file: {destination_path}")

def get_paths():
    source_path = input("Enter the source file path: ").strip()
    destination_directory = input("Enter the destination directory path: ").strip()
    return source_path, destination_directory

source_file, destination_folder = get_paths()

# Perform the first backup immediately.
perform_backup(source_file, destination_folder)

# Schedule subsequent backups every hour.
schedule.every(1).hour.do(
    perform_backup,
    source_path=source_file,
    destination_directory=destination_folder
)

print("File backup scheduled every hour.")
print("Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(1)
