import schedule
import time

def displayMessage(message):
    print(message)

def main():
    message = input("Enter message: ").strip()

    schedule.every(5).seconds.do(displayMessage, message)

    print("Message scheduled every 5 seconds.")
    print("Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
