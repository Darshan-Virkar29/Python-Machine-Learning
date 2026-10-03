import schedule
import time
from datetime import datetime

def create_file():
    now=datetime.now()
    stamp=now.strftime("%d_%m_%Y_%H_%M_%S")
    name=f"File_{stamp}.txt"
    with open(name,"w",encoding="utf-8") as f:
        f.write(f"Filename: {name}\n")
        f.write(f"Creation Date: {now.strftime('%d-%m-%Y')}\n")
        f.write(f"Creation Time: {now.strftime('%I:%M:%S %p')}\n")
    print(f"Created: {name}")

create_file()
schedule.every(1).minute.do(create_file)
print("Creating a new timestamped text file every minute. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)
