import os
import shutil
from datetime import datetime

def sort_by_file_type(directory):
    try:
        for file in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file)):
                ext = file.split('.')[-1]
                ext_dir = os.path.join(directory, ext.upper() + "_Files")
                if not os.path.exists(ext_dir):
                    os.mkdir(ext_dir)
                shutil.move(os.path.join(directory, file), os.path.join(ext_dir, file))
        print("Files sorted by type successfully.")
    except Exception as e:
        print(f"Error sorting by file type: {str(e)}")

def sort_by_date(directory):
    try:
        for file in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file)):
                modification_time = os.path.getmtime(os.path.join(directory, file))
                date_folder = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d')
                date_dir = os.path.join(directory, date_folder)
                if not os.path.exists(date_dir):
                    os.mkdir(date_dir)
                shutil.move(os.path.join(directory, file), os.path.join(date_dir, file))
        print("Files sorted by date successfully.")
    except Exception as e:
        print(f"Error sorting by date: {str(e)}")

def main():
    user_name = input("Please enter your name: ").strip()
    print(f"Welcome to the File Format Terminal App, {user_name}!")
    directory = input("What folder would you like to sort? ").strip()

    if not os.path.exists(directory):
        print("The specified directory does not exist. Please check the path and try again.")
        return

    print("How would you like to format the files?")
    print("1: By file type")
    print("2: By modification date")
    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':
        sort_by_file_type(directory)
    elif choice == '2':
        sort_by_date(directory)
    else:
        print("Invalid input. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
