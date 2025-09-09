import os
import shutil

# Dictionary to map file extensions to folder names
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".m4a", ".flac"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".java", ".cpp", ".html", ".css"],
    "Others": []
}


def get_folder_for_file(filename):
    ext = os.path.splitext(filename)[1].lower()
    for folder, extensions in FILE_TYPES.items():
        if ext in extensions:
            return folder
    return "Others"


def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f"❌ Folder '{folder_path}' does not exist.")
        return

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            folder_name = get_folder_for_file(item)
            new_folder_path = os.path.join(folder_path, folder_name)

            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)

            shutil.move(item_path, os.path.joi_
