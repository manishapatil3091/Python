import os
import shutil
import schedule
import time

def CopyFiles(src,dest):

    if not os.path.isdir(src):
        print("Invalid Source Directory")
        return

    if not os.path.isdir(dest):
        print("Invalid Destination Directory")
        return

    with open("CopyLog.txt","a") as log:

        for file in os.listdir(src):

            if file.endswith(".txt"):

                source = os.path.join(src,file)
                destination = os.path.join(dest,file)

                try:
                    shutil.copy2(source,destination)

                    log.write(file+" Copied Successfully\n")

                except Exception:
                    log.write(file+" Copy Failed\n")

    print("Copy Completed")

def main():

    src = input("Enter Source Directory : ")
    dest = input("Enter Destination Directory : ")

    schedule.every(10).minutes.do(CopyFiles,src,dest)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()