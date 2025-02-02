import os
import shutil
import win32file
import win32con
import re
from datetime import datetime
import pytz

# Define possible year matches (last 50 years)
CURRENT_YEAR = datetime.now().year
POSSIBLE_YEARS = {str(year) for year in range(CURRENT_YEAR - 50, CURRENT_YEAR + 1)}

# Define file categories
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.HEIC'}
VIDEO_EXTENSIONS = {'.mp4', '.mkv', '.mov', '.avi', '.flv', '.wmv'}


# Timezone for Germany (CET/CEST)
germany_timezone = pytz.timezone('Europe/Berlin')

def get_file_timestamps(file_path):
    """Retrieve both creation and modification timestamps using Windows API for consistency."""
    handle = win32file.CreateFile(
        file_path,
        win32con.GENERIC_READ,
        win32con.FILE_SHARE_READ,
        None,
        win32con.OPEN_EXISTING,
        0,
        None
    )

    # Get file times (creation, last access, last modified)
    creation_time, _, mod_time = win32file.GetFileTime(handle)
    handle.Close()

    # Convert pywintypes.datetime to regular datetime using timestamp()
    # and convert them to timezone-aware datetime objects
    creation_time = datetime.fromtimestamp(creation_time.timestamp(), germany_timezone)
    mod_time = datetime.fromtimestamp(mod_time.timestamp(), germany_timezone)

    return creation_time, mod_time


def determine_date(file_path):
    """Determine the correct creation date of a file, considering copied files."""
    try:
        creation_time, mod_time = get_file_timestamps(file_path)

        print(f"\n📂 Checking file: {file_path}")
        print(f"🟢 Creation Date: {creation_time}")
        print(f"🟡 Last Modified Date: {mod_time}")

        # If creation date is before modification date, use it normally
        if creation_time <= mod_time:
            return creation_time

        print("⚠️ Possible copied file detected! Checking for year in filename...")

        # Search for a year in the filename
        file_name = os.path.basename(file_path)
        # Find all matches of years (1900-2099)
        matches = re.findall(r'(19\d{2}|20\d{2})', file_name)

        if matches:
            # Loop through each found year
            for found_year in matches:
                if found_year in POSSIBLE_YEARS:
                    user_input = input(f"🔍 Found year '{found_year}' in filename: '{file_name}'. Use this as creation year? (y/n): ")
                    if user_input.lower() == 'y':
                        return datetime(int(found_year), 1, 1)  # Assume Jan 1st of that year

        # If no valid year is found in the name or user didn't select a year
        print("❌ No valid year found or user skipped. 🔄 Using last modified date.")
        return mod_time

    except Exception as e:
        print(f"❌ Error retrieving date for {file_path}: {e}")
        return None


def get_unique_filename(dest_folder, file_name):
    """Rename file as originalname_duplicate_1.ext if duplicate exists."""
    base, ext = os.path.splitext(file_name)
    counter = 1
    new_name = f"{base}_duplicate_{counter}{ext}"

    while os.path.exists(os.path.join(dest_folder, new_name)):
        counter += 1
        new_name = f"{base}_duplicate_{counter}{ext}"

    return new_name

def check_and_rename_directory(directory_path):
    # Check if the directory exists
    if os.path.exists(directory_path):
        # Get the directory name and parent directory
        parent_dir = os.path.dirname(directory_path)
        dir_name = os.path.basename(directory_path)

        # Check if the directory is empty
        if not os.listdir(directory_path):
            # If the directory is empty, append '_empty' to its name
            new_name = dir_name + "_empty"
            new_path = os.path.join(parent_dir, new_name)
            os.rename(directory_path, new_path)
            print(f"Directory is empty. Renamed to: {new_path}")
        else:
            # If the directory is not empty, append '_check_remaining_files' to its name
            new_name = dir_name + "_check_remaining_files"
            new_path = os.path.join(parent_dir, new_name)
            os.rename(directory_path, new_path)
            print(f"Directory is not empty. Renamed to: {new_path}")
    else:
        print(f"The directory at {directory_path} does not exist.")

def sort_files_by_year(directory, destination_dir):
    """Sorts files into year-based subfolders with categories for images, videos, and files."""
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Determine file date
            date = determine_date(file_path)
            if not date:
                print(f"⚠️ Skipping {file_path}, unable to determine date.")
                continue

            year = date.year

            # Define category subfolder
            _, ext = os.path.splitext(file_name)
            ext = ext.lower()
            if ext in IMAGE_EXTENSIONS:
                category = "Images"
            elif ext in VIDEO_EXTENSIONS:
                category = "Videos"
            else:
                category = "Files"

            # Create year & category folders if they don't exist
            year_folder = os.path.join(destination_dir, str(year), category)
            os.makedirs(year_folder, exist_ok=True)

            # Check for duplicates & rename if necessary
            destination_path = os.path.join(year_folder, file_name)
            if os.path.exists(destination_path):
                new_file_name = get_unique_filename(year_folder, file_name)
                destination_path = os.path.join(year_folder, new_file_name)

            shutil.move(file_path, destination_path)
            print(f"✅ Moved: {file_path} -> {destination_path}")



# 🔹 Change these paths before running
#source_folder = r"C:\Users\tim\Desktop\AUS Job"
#destination_folder = r"C:\Users\tim\Desktop\Sorted"

destination_folder = r"C:\Users\tim\Desktop\AUS Job"
source_folder = r"C:\Users\tim\Desktop\Sorted"


sort_files_by_year(source_folder, destination_folder)