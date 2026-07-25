import os
import schedule
import time
import datetime

def FileSize(path):
    try:
        size = os.path.getsize(path)

        with open("FileSizeLog.txt", "a") as fobj:
            fobj.write(f"File : {path}\n")
            fobj.write(f"Size : {size} Bytes\n")
            fobj.write(f"Date & Time : {datetime.datetime.now()}\n")
            fobj.write("-"*40+"\n")

        print("Log Updated")

    except FileNotFoundError:
        print("File does not exist.")

def main():

    path = input("Enter file path : ")

    schedule.every(30).seconds.do(FileSize, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()