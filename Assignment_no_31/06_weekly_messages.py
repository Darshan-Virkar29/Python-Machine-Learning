import schedule
import time

def start_weekly_goals():
    print("Start your weekly goals")

def review_weekly_progress():
    print("Review your weekly progress")

def weekly_work_completed():
    print("Weekly work completed")

# Monday at 9:00 AM
schedule.every().monday.at("09:00").do(start_weekly_goals)

# Wednesday at 5:00 PM
schedule.every().wednesday.at("17:00").do(review_weekly_progress)

# Friday at 6:00 PM
schedule.every().friday.at("18:00").do(weekly_work_completed)

print("Weekly messages scheduled:")
print("Monday 09:00 AM  - Start your weekly goals")
print("Wednesday 05:00 PM - Review your weekly progress")
print("Friday 06:00 PM - Weekly work completed")
print("Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(1)
