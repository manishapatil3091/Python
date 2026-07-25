import schedule
import time
import datetime

def Display():
    print("Namskar...")

def main():
    print("Automation Script Started")

    
    schedule.every().day.at("09:00:00").do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
