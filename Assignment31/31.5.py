import os
import schedule
import time
import datetime

def DirectoryCount(path):
    try:
        count = 0

        for Fname in os.listdir(path):
            fullpath = os.path.join(path, Fname)

            if os.path.isfile(fullpath):
                count = count + 1

        with open("DirectoryCountLog.txt", "a") as fobj:
            fobj.write(f"\nDirectory Path : {path}\n")
            fobj.write(f"Number of Files : {count}\n")
            fobj.write(f"Date & Time : {datetime.datetime.now()}\n")
            fobj.write("-" * 50 + "\n")

        print("Log Updated Successfully.")

    except FileNotFoundError:
        print("Directory not found.")

def main():
    print("Automation Script Started...")
    path = input("Enter Directory Path : ")

    schedule.every(5).minutes.do(DirectoryCount, path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
