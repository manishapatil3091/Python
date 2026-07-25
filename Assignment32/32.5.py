import os
import schedule
import time

def DeleteEmpty(path):

    with open("DeleteLog.txt","a") as log:

        for folder,subfolder,files in os.walk(path):
            for Fname in files:
                filepath = os.path.join(folder,Fname)
                try:
                    if os.path.getsize(filepath) == 0:
                        os.remove(filepath)
                        log.write(filepath+" Deleted\n")

                except PermissionError:
                    log.write(filepath+" Permission Denied\n")

                except Exception:
                    log.write(filepath+" Error\n")

    print("Empty File Scan Completed")

def main():

    path = input("Enter Directory : ")

    schedule.every(1).hours.do(DeleteEmpty,path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()