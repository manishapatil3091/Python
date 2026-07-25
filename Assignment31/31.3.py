import os
import schedule
import time
import datetime

def ScanDirectory(path):
    try:
        Fno = 0
        SubNo = 0

        for Fname in os.listdir(path):
            full_path = os.path.join(path, Fname)

            if os.path.isfile(full_path):
                Fno = Fno + 1
            elif os.path.isdir(full_path):
                SubNo = SubNo + 1

        print("\nDirectory Scanned :", path)
        print("Total Files :", Fno)
        print("Total Subdirectories :", SubNo)
        print("Scan Time :", datetime.datetime.now())

    except FileNotFoundError:
        print("Directory not found.")

def main():
    path = input("Enter directory path : ")

    schedule.every(1).minutes.do(ScanDirectory, path)

    print("Automation Script Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
