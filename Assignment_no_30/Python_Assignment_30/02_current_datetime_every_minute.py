import schedule
import time
from datetime import datetime

def print_current_datetime():
    current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    print(f"Current Date and Time: {current_time}")

schedule.every(1).minute.do(print_current_datetime)

print("Displaying current date and time every minute. Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(1)
