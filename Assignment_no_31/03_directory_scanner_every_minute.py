import os
import schedule
import time
from datetime import datetime

def scan_directory(directory_path):
    if not os.path.isdir(directory_path):
        print(f"Directory does not exist: {directory_path}")
        return

    entries = os.listdir(directory_path)

    file_count = sum(
        1 for entry in entries
        if os.path.isfile(os.path.join(directory_path, entry))
    )

    subdirectory_count = sum(
        1 for entry in entries
        if os.path.isdir(os.path.join(directory_path, entry))
    )

    scan_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    print("\nDirectory Scan")
    print("-" * 35)
    print(f"Directory Scanned: {directory_path}")
    print(f"Total Files: {file_count}")
    print(f"Total Subdirectories: {subdirectory_count}")
    print(f"Scan Time: {scan_time}")

def main():
    directory_path = input("Enter directory path to scan: ").strip()

    # Scan immediately once.
    scan_directory(directory_path)

    # Scan every minute.
    schedule.every(1).minute.do(scan_directory, directory_path)

    print("\nDirectory scanning scheduled every minute.")
    print("Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
