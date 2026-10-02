import os
import schedule
import time
from datetime import datetime

LOG_FILE = "DirectoryCountLog.txt"

def count_files(directory_path):
    if not os.path.isdir(directory_path):
        print(f"Directory does not exist: {directory_path}")
        return

    file_count = sum(
        1 for entry in os.listdir(directory_path)
        if os.path.isfile(os.path.join(directory_path, entry))
    )

    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"Directory Path: {directory_path}\n")
        file.write(f"Number of Files: {file_count}\n")
        file.write(f"Date and Time: {current_time}\n")
        file.write("-" * 40 + "\n")

    print("\nDirectory Count")
    print("-" * 30)
    print(f"Directory Path: {directory_path}")
    print(f"Number of Files: {file_count}")
    print(f"Date and Time: {current_time}")

def main():
    directory_path = input("Enter directory path: ").strip()

    # Count immediately once.
    count_files(directory_path)

    # Repeat every five minutes.
    schedule.every(5).minutes.do(count_files, directory_path)

    print("\nFile counting scheduled every 5 minutes.")
    print(f"Results are written to {LOG_FILE}.")
    print("Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
