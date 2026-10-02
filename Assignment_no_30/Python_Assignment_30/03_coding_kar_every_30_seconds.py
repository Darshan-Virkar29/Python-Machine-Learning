import schedule
import time

def print_coding_kar():
    print("Coding Kar...")

schedule.every(30).seconds.do(print_coding_kar)

print("Printing 'Coding Kar...' every 30 seconds. Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(1)
