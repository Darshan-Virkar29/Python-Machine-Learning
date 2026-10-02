import schedule
import time
from datetime import datetime

FILE_NAME = "Marvellous.txt"

def write_current_datetime():
    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(f"Task executed at: {current_time}\n")

    print(f"Task executed at: {current_time}")
    print(f"Date and time appended to {FILE_NAME}")

# Run once after 5 minutes.
schedule.every(5).minutes.do(write_current_datetime)

print("Task scheduled to execute every 5 minutes.")
print("Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(1)
