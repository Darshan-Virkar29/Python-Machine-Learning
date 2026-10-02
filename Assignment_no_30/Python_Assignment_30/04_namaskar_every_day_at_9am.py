import schedule
import time

def print_namaskar():
    print("Namaskar...")

schedule.every().day.at("09:00").do(print_namaskar)

print("Task scheduled daily at 09:00 AM. Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(1)
