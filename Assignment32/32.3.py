import schedule
import time

def ReadFile(path):

    try:
        with open(path,"r") as fobj:

            data = fobj.read()

            if len(data) == 0:
                print("File is empty.")
            else:
                print(data)

    except FileNotFoundError:
        print("File does not exist.")

    except PermissionError:
        print("Permission denied.")

    except OSError:
        print("File cannot be opened.")

def main():

    path = input("Enter file path : ")

    schedule.every(1).minutes.do(ReadFile,path)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()