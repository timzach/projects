import os
import shutil
from datetime import datetime

def get_unique_filename(dest_folder, file_name):
    """Rename file as originalname_duplicate_1.ext if duplicate exists."""
    base, ext = os.path.splitext(file_name)
    counter = 1
    new_name = f"{base}_duplicate_{counter}{ext}"

    while os.path.exists(os.path.join(dest_folder, new_name)):
        counter += 1
        new_name = f"{base}_duplicate_{counter}{ext}"

    return new_name

def sort_files_by_year(directory):
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            timestamp = os.path.getctime(file_path)
            year = datetime.fromtimestamp(timestamp).year

            # Create year folder if it doesn't exist
            year_folder = os.path.join(directory, str(year))
            if not os.path.exists(year_folder):
                os.makedirs(year_folder)

            # Check for duplicates & rename only if necessary
            destination_path = os.path.join(year_folder, file_name)
            if os.path.exists(destination_path):
                new_file_name = get_unique_filename(year_folder, file_name)
                destination_path = os.path.join(year_folder, new_file_name)

            shutil.move(file_path, destination_path)
            print(f"Moved: {file_path} -> {destination_path}")

# Example usage
sort_files_by_year('C:\\Users\\tim\\Desktop\\AUS Job')

