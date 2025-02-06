import os
import shutil
import re

# Path to the log file
log_file = "log.txt"


def reverse_file_moves(log_file):
    with open(log_file, "r", encoding="utf-8") as file:
        for line in file:
            match = re.match(r"Moved: (.*?) -> (.*?)$", line.strip())
            if match:
                original_path, moved_path = match.groups()

                # Check if the moved file exists before moving it back
                if os.path.exists(moved_path):
                    os.makedirs(os.path.dirname(original_path), exist_ok=True)
                    shutil.move(moved_path, original_path)
                    print(f"Moved back: {moved_path} -> {original_path}")
                else:
                    print(f"File not found, skipping: {moved_path}")


if __name__ == "__main__":
    reverse_file_moves(log_file)
