import os
import schedule
import time
from datetime import datetime

def create_log_file():
    now = datetime.now()
    timestamp = now.strftime("%d_%m_%Y_%H_%M_%S")
    display_time = now.strftime("%d-%m-%Y %I:%M:%S %p")

    filename = f"MarvellousLog_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("Log file created successfully.\n")
        file.write(f"Creation Time: {display_time}\n")

    print(f"Log file created successfully: {filename}")
    print(f"Creation Time: {display_time}")

# Create one immediately.
create_log_file()

# Create a new log file every 10 minutes.
schedule.every(10).minutes.do(create_log_file)

print("New log file scheduled every 10 minutes.")
print("Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(1)
