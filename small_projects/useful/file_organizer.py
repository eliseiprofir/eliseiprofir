import os
import shutil


def create_subfolder_if_needed(folder_path: str, subfolder_name: str) -> str:
    subfolder_path: str = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path


def clean_folder(folder_path: str) -> None:
    for filename in os.listdir(folder_path):
        if filename == os.path.basename(__file__):
            continue
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = filename.split('.')[-1].lower()
            if file_extension:
                subfolder_name: str = f"{file_extension.upper()} Files"
                subfolder_path: str = create_subfolder_if_needed(folder_path, subfolder_name)
                file_path: str = os.path.join(folder_path, filename)
                shutil.move(file_path, subfolder_path)
                print(f"Moved: {filename} -> {subfolder_name}")
            

if __name__ == "__main__":
    print("This program will organize your files in the folder you put it in.")
    input("Hit enter to start... ")
    path: str = os.getcwd()
    clean_folder(path)
    print("Files organized successfully")
    input("Hit enter to quit the program...")
