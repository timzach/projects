import os
import re
from datetime import datetime
from PIL import Image
import imagehash
import difflib
import pdfplumber
import docx

# Configurations
LOG_FILE = f"duplicate_check_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
TESTING_MODE = True  # Set to False after testing
SKIPPED_FILES = []  # Store skipped files


def log_message(message):
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(message + "\n")
    print(message)


def find_duplicates(directory):
    """Finds and groups files with the _duplicate_X naming pattern."""
    file_groups = {}
    pattern = re.compile(r"(.*)_duplicate_(\d+)(\..+)")

    for root, _, files in os.walk(directory):
        for file_name in files:
            match = pattern.match(file_name)
            if match:
                base_name = match.group(1) + match.group(3)  # Original filename without duplicate tag
                full_path = os.path.join(root, file_name)
                file_groups.setdefault(base_name, []).append(full_path)

    return {k: v for k, v in file_groups.items() if len(v) > 1}  # Only return actual duplicates


def get_image_hash(image_path):
    """Generate a perceptual hash for an image."""
    try:
        with Image.open(image_path) as img:
            return imagehash.average_hash(img)
    except Exception as e:
        log_message(f"Skipping file (not an image): {image_path}")
        SKIPPED_FILES.append(image_path)
        return None


def compare_text_files(files):
    """Compare multiple text-based files and return if they are identical."""
    try:
        texts = [open(f, "r", encoding="utf-8").readlines() for f in files]
        return all(difflib.SequenceMatcher(None, texts[0], text).ratio() > 0.95 for text in texts[1:])
    except Exception as e:
        log_message(f"Error comparing text files: {e}")
        SKIPPED_FILES.extend(files)
        return False


def compare_pdfs(files):
    """Extract text from PDFs and compare similarity."""
    try:
        texts = []
        for pdf in files:
            with pdfplumber.open(pdf) as doc:
                texts.append(" ".join([page.extract_text() or "" for page in doc.pages]))
        return all(difflib.SequenceMatcher(None, texts[0], text).ratio() > 0.95 for text in texts[1:])
    except Exception as e:
        log_message(f"Error comparing PDFs: {e}")
        SKIPPED_FILES.extend(files)
        return False


def compare_word_docs(files):
    """Extract text from Word files and compare similarity."""
    try:
        texts = [" ".join([p.text for p in docx.Document(f).paragraphs]) for f in files]
        return all(difflib.SequenceMatcher(None, texts[0], text).ratio() > 0.95 for text in texts[1:])
    except Exception as e:
        log_message(f"Error comparing Word documents: {e}")
        SKIPPED_FILES.extend(files)
        return False


def compare_file_sizes(files):
    """Compare file sizes for non-supported types."""
    sizes = [os.path.getsize(f) for f in files]
    return all(size == sizes[0] for size in sizes[1:])


def suggest_best_file(files):
    """Check if files are identical; otherwise, let user decide."""
    if all(f.lower().endswith(('.jpg', '.jpeg', '.png')) for f in files):
        hashes = [get_image_hash(f) for f in files]
        if all(h == hashes[0] for h in hashes if h is not None):
            return files[0]
    elif all(f.lower().endswith('.txt') for f in files) and compare_text_files(files):
        return files[0]
    elif all(f.lower().endswith('.pdf') for f in files) and compare_pdfs(files):
        return files[0]
    elif all(f.lower().endswith('.docx') for f in files) and compare_word_docs(files):
        return files[0]

    user_choice = input(f"File type not supported. Do you want to delete duplicates and keep {files[0]}? (y/n): ")
    if user_choice.lower() == 'y':
        return files[0]
    return None

def log_skipped_files():
    """Logs all skipped files at the end of execution."""
    if SKIPPED_FILES:
        log_message("\nSkipped files:")
        for file in SKIPPED_FILES:
            log_message(file)


def handle_duplicates(duplicates):
    """Processes all duplicate sets."""
    if not duplicates:
        log_message("No duplicates found.")
        return

    for original_file, duplicate_files in duplicates.items():
        all_files = [os.path.join(os.path.dirname(duplicate_files[0]), original_file)] + duplicate_files
        log_message("\nDuplicate set found:")
        for i, file in enumerate(all_files, start=1):
            log_message(f"{i}) {file}")

        suggested_file = suggest_best_file(all_files)
        if suggested_file:
            for file in all_files:
                if file != suggested_file:
                    os.remove(file)
                    log_message(f"Deleted: {file}")
            log_message(f"Kept: {suggested_file}")
        else:
            log_message("Files are not identical, user must decide.")

    log_skipped_files()


# Main execution
directory_to_check = "D:\\Sorted"
duplicates = find_duplicates(directory_to_check)
handle_duplicates(duplicates)
