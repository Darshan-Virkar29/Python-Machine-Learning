import schedule
import time

def print_jay_ganesh():
    print("Jay Ganesh...")

schedule.every(2).seconds.do(print_jay_ganesh)

print("Printing 'Jay Ganesh...' every 2 seconds. Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(1)
