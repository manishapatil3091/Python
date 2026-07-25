import schedule
import time
import datetime

def CreateFile():
    now = datetime.datetime.now()

    filename = "File_" + now.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"


    timestamp = time.ctime()
    FileName = "File_%s.log"%(timestamp)  # %s wwill get replace
    FileName = FileName.replace(" ","_")
    FileName = FileName.replace(":","_")

    with open(filename, "w") as fobj:
        fobj.write(f"Filename : {filename}\n")
        fobj.write(f"Creation Date : {now.strftime('%d-%m-%Y')}\n")
        fobj.write(f"Creation Time : {now.strftime('%I:%M:%S %p')}\n")

    print(filename, "created successfully.")

def main():

    print("Automation Script Started...")

    schedule.every(1).minutes.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()