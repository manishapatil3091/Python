import schedule
import time
import datetime

def Display(message):
    print(message)

def main():
    print("Automation Script Started")
    message = input("Enter message: ")
    interval = int(input("Enter interval in seconds: "))

    schedule.every(interval).seconds.do(Display,message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
