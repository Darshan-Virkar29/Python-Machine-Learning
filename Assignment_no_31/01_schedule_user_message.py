import schedule
import time

def display_message(message):
    print(message)

def main():
    message = input("Enter message: ").strip()

    try:
        interval = int(input("Enter interval in seconds: "))
    except ValueError:
        print("Please enter a valid integer for the interval.")
        return

    if interval <= 0:
        print("Interval must be greater than zero.")
        return

    schedule.every(interval).seconds.do(display_message, message)

    print(f"Message scheduled every {interval} seconds.")
    print("Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
