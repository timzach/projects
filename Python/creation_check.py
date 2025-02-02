import os
import win32file
import win32con
import pywintypes
from datetime import datetime, timezone
from PIL import Image
from PIL.ExifTags import TAGS


def get_windows_creation_date(file_path):
    """Retrieve the creation date of a file on Windows."""
    try:
        handle = win32file.CreateFile(
            file_path,
            win32con.GENERIC_READ,
            win32con.FILE_SHARE_READ,
            None,
            win32con.OPEN_EXISTING,
            0,
            None
        )
        creation_time = win32file.GetFileTime(handle)[0]  # Get creation time (UTC)
        handle.Close()

        return creation_time.replace(tzinfo=timezone.utc).astimezone()  # Convert to local time
    except pywintypes.error as e:
        print(f"Error retrieving creation date: {e}")
        return None


def get_exif_creation_date(file_path):
    """Try to get the original creation date from EXIF metadata (for images)."""
    try:
        image = Image.open(file_path)
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name in ["DateTimeOriginal", "CreateDate"]:
                    return datetime.strptime(value, "%Y:%m:%d %H:%M:%S").replace(tzinfo=timezone.utc).astimezone()
    except Exception as e:
        print(f"EXIF metadata not found or unreadable: {e}")
    return None


def check_file_date(file_path):
    """Check if a file was copied and try to recover its original date."""
    if not os.path.exists(file_path):
        print("File not found. Please check the path and try again.")
        return

    print(f"\nChecking file: {file_path}")

    # Get the "Windows creation date"
    creation_date = get_windows_creation_date(file_path)

    # Get last modified date and make it timezone-aware
    mod_time = datetime.fromtimestamp(os.path.getmtime(file_path), tz=timezone.utc).astimezone()

    # Check if the file was copied (creation date is newer than last modified date)
    if creation_date and creation_date > mod_time:
        print("⚠️ Possible copied file detected! Trying to find the original date...")

        # Try to get EXIF data for images
        if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff', '.gif')):
            exif_date = get_exif_creation_date(file_path)
            if exif_date:
                print(f"✅ Original Creation Date (from EXIF): {exif_date}")
                return

        # Fallback: Use last modified time instead
        print(f"🔄 Using Last Modified Date as original creation date: {mod_time}")
    else:
        print(f"✅ Original Creation Date: {creation_date}")

    print(f"🕒 Last Modified Date: {mod_time}")


# 🔹 Change this path to test
test_file = r"C:\Users\tim\Desktop\AUS Job\2025\IMG_6012.jpg"

check_file_date(test_file)
