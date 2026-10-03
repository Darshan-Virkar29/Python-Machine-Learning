import os
import schedule
import time
from datetime import datetime

def monitor(path):
    now=datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    if not os.path.isfile(path):
        msg=f"File Path: {path}\nStatus: File does not exist\nDate and Time: {now}\n"
    else:
        msg=f"File Path: {path}\nFile Size in Bytes: {os.path.getsize(path)}\nDate and Time: {now}\n"
    print(msg)
    with open("FileSizeLog.txt","a",encoding="utf-8") as log:
        log.write(msg+"-"*40+"\n")

path=input("Enter file path: ").strip()
monitor(path)
schedule.every(30).seconds.do(monitor,path)
print("Monitoring every 30 seconds. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)
