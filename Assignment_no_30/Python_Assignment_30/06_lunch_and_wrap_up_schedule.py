import schedule
import time

def print_lunch_time():
    print("Lunch Time!")

def print_wrap_up():
    print("Wrap up work")

# Both tasks are handled by separate functions.
schedule.every().day.at("13:00").do(print_lunch_time)
schedule.every().day.at("18:00").do(print_wrap_up)

print("Lunch Time! scheduled daily at 01:00 PM.")
print("Wrap up work scheduled daily at 06:00 PM.")
print("Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(1)
