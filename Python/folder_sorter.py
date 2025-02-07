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
FILE_CATEGORIES = {
    "images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".heic"},
    "videos": {".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv"},
    "office_files": {".txt", ".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".csv", ".ods", ".ppt", ".pptx", ".odp"},
    "compressed": {".zip", ".rar", ".7z", ".tar.gz"},
    "code": {".py", ".java", ".js", ".cpp", ".html", ".css"},
    "executables": {".exe", ".msi"}
}
OTHER_FOLDER = "other"  # Folder for unknown extensions

# Timezone for Germany (CET/CEST)
germany_timezone = pytz.timezone('Europe/Berlin')

# Log file
LOG_FILE = f"C:\\Users\\tim\\Projects\\logs\\file_sorting_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

def log_message(message):
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(message + "\n")
    print(message)


# Log script start time
log_message(f"Script started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def get_file_timestamps(file_path):
    """Retrieve both creation and modification timestamps using Windows API."""
    handle = win32file.CreateFile(file_path, win32con.GENERIC_READ, win32con.FILE_SHARE_READ, None,
                                  win32con.OPEN_EXISTING, 0, None)
    creation_time, _, mod_time = win32file.GetFileTime(handle)
    handle.Close()
    return datetime.fromtimestamp(creation_time.timestamp(), germany_timezone), datetime.fromtimestamp(
        mod_time.timestamp(), germany_timezone)


def determine_date(file_path):
    """Determine the correct creation date of a file."""
    try:
        creation_time, mod_time = get_file_timestamps(file_path)
        if creation_time.year <= mod_time.year:
            return creation_time
        filename = os.path.basename(file_path)
        matches = re.findall(r'(19\d{2}|20\d{2})', filename)
        for found_year in matches:
            if int(found_year) in range(CURRENT_YEAR - 50, CURRENT_YEAR + 1) and int(found_year) != mod_time.year:
                user_input = input(f"Found year '{found_year}' in {filename} with modification in {mod_time.year}. Use this as creation year? (y/n): ")
                if user_input.lower() == 'y':
                    return datetime(int(found_year), 1, 1)
        return mod_time
    except Exception as e:
        log_message(f"Error retrieving date for {file_path}: {e}")
        return None


def get_unique_filename(dest_folder, file_name):
    """Generate a unique filename if a duplicate exists."""
    base, ext = os.path.splitext(file_name)
    counter = 1
    new_name = f"{base}_duplicate_{counter}{ext}"
    while os.path.exists(os.path.join(dest_folder, new_name)):
        counter += 1
        new_name = f"{base}_duplicate_{counter}{ext}"
    return new_name


def get_category(ext):
    """Determine the category folder based on file extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return OTHER_FOLDER


def sort_files_by_year(source_dir, destination_dir):
    """Sorts files into categorized folders with year subfolders."""
    for root, _, files in os.walk(source_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            date = determine_date(file_path)
            if not date:
                continue

            year_folder = os.path.join(destination_dir, get_category(os.path.splitext(file_name)[1].lower()),
                                       str(date.year))
            os.makedirs(year_folder, exist_ok=True)

            destination_path = os.path.join(year_folder, file_name)
            if os.path.exists(destination_path):
                destination_path = os.path.join(year_folder, get_unique_filename(year_folder, file_name))

            shutil.move(file_path, destination_path)
            log_message(f"Moved: {file_path} -> {destination_path}")


def delete_empty_folders(directory):
    """Recursively deletes all completely empty folders."""

    def remove_empty_dirs(path):
        removed = False
        for root, dirs, _ in os.walk(path, topdown=False):
            for d in dirs:
                dir_path = os.path.join(root, d)
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
                    removed = True
        return removed

    while remove_empty_dirs(directory):
        pass

    if not os.listdir(directory):
        log_message(f"The root directory is now empty: {directory}")


# Change these paths before running
source_folder_location = r"C:\Users\tim\OneDrive_download\Bilder\Katzen"
destination_folder = r"D:\Sorted"
source_folders = ['iCloud Fotos']


if __name__ == "__main__":
    for folder in source_folders:
        sort_files_by_year(os.path.join(source_folder_location, folder), destination_folder)
        delete_empty_folders(os.path.join(source_folder_location, folder))