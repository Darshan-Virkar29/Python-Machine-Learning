import os
import shutil
import schedule
import time
from datetime import datetime

def copy_files(source,destination):
    now=datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    if not os.path.isdir(source):
        print("Source directory does not exist.")
        return
    if not os.path.isdir(destination):
        print("Destination directory does not exist.")
        return

    count=0
    for name in os.listdir(source):
        src=os.path.join(source,name)
        dst=os.path.join(destination,name)
        if name.lower().endswith(".txt") and os.path.isfile(src):
            try:
                shutil.copy2(src,dst)
                count+=1
                print("Copied:",name)
            except (OSError,PermissionError) as e:
                print(f"Could not copy {name}: {e}")

    with open("CopyLog.txt","a",encoding="utf-8") as log:
        log.write(f"Date and Time: {now}\nFiles Copied: {count}\n{'-'*40}\n")
    print(f"Copied {count} .txt file(s) at {now}.")

source=input("Enter source directory: ").strip()
destination=input("Enter destination directory: ").strip()
copy_files(source,destination)
schedule.every(10).minutes.do(copy_files,source,destination)
print("Copying .txt files every 10 minutes. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)
