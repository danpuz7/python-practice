import os 
import shutil
import datetime
import schedule
import time
from pytz import timezone

source_dir = "/Users/danielpuzan/Photos"
destination_dir = "/Users/danielpuzan/Backup"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {destination_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

schedule.every().day.at("08:16", timezone("US/Central")).do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)

