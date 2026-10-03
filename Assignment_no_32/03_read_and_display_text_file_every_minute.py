import os
import schedule
import time

def read_file(path):
    print("\n"+"="*50)
    if not os.path.exists(path):
        print("Error: File does not exist.")
    elif os.path.isdir(path):
        print("Error: File cannot be opened because the path is a directory.")
    elif os.path.getsize(path)==0:
        print("Error: File is empty.")
    else:
        try:
            with open(path,"r",encoding="utf-8") as f:
                print(f.read())
        except PermissionError:
            print("Error: Permission is denied.")
        except OSError as e:
            print(f"Error: File cannot be opened. {e}")
    print("="*50)

path=input("Enter text file path: ").strip()
read_file(path)
schedule.every(1).minute.do(read_file,path)
print("Reading file every minute. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)
