import schedule
import time
import shutil
import os
import datetime

def Backup(SourceFile, DestinationFolder):
    try:
        # Get source file name and extension
        filename = os.path.basename(SourceFile)
        name, ext = os.path.splitext(filename)

        # Create backup file name
        backup_file = f"{name}_{datetime.datetime.now()}{ext}"
        destination_path = os.path.join(DestinationFolder, backup_file)

        # Copy file
        shutil.copy2(SourceFile, destination_path)

        # Write log
        with open("backup_log.txt", "a") as log:
            log.write(f"Backup completed successfully at {datetime.datetime.now()}\n")

        print("Backup completed successfully.")

    except FileNotFoundError:
        print("Source file not found.")
    except Exception as e:
        print("Error:", e)


def main():
    source = input("Enter source file path: ")
    destination = input("Enter destination folder path: ")

    print("Automatic Backup Started...")

    # Perform backup every hour
    schedule.every(1).hours.do(Backup, source, destination)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()