import schedule
import time
import datetime

def WeeklyGoals():
    print(datetime.datetime.now())
    print("Start your weekly goals")

def ReviewProgress():
    print(datetime.datetime.now())
    print("Review your weekly progress")
    
def WeeklyCompleted():
    print(datetime.datetime.now())
    print("Weekly work completed")

def main():
    print("Automation Script Started...")

    schedule.every().monday.at("09:00:00").do(WeeklyGoals)
    schedule.every().wednesday.at("17:00:00").do(ReviewProgress)
    schedule.every().friday.at("18:00:00").do(WeeklyCompleted)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()