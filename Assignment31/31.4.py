import schedule
import time
import datetime

def CreateLog():
    filename = "MarvellousLog_" + datetime.datetime.now() + ".txt"

    with open(filename, "w") as fobj:
        fobj.write("Log file created successfully.\n")
        fobj.write("Creation Time : ")
        fobj.write(datetime.datetime.now())

    print(filename, "created successfully.")

def main():
    print("Automation Script Started...")

    schedule.every(10).minutes.do(CreateLog)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()