import os
import shutil

def separate_and_move_files(source_folder, destination_folder, file_extension):
    
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    files = os.listdir(source_folder)

    for file in files:
        if file.endswith(file_extension):
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)

            shutil.move(source_path, destination_path)
            print(f"Moved file: {file}")


source_folder = "./mbMusic"
destination_folder = "onlyMp3Files"
file_extension = (".mp3", ".MP3", "m4a")

separate_and_move_files(source_folder, destination_folder, file_extension)
print("Mp3 files separated successfully.")