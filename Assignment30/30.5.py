import schedule
import time
import datetime

def CurrentDateTme():

    fobj = open("Marvellous.txt","a")
    data = datetime.datetime.now()
    fobj.write("Task executed at : "+ str(data) + "\n")

def main():
    print("Automation Script Started")

    schedule.every(5).minutes.do(CurrentDateTme)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
