import os
import shutil
from tinytag import TinyTag
import re

mb_music_folder = './mbMusic'
renamed_music_folder = './managedMusic'

special_characters = r'[._()\[\]!@#$%^&*+=|;:"<>,?/\\-]+$'

music_files = []
for root, dirs, files in os.walk(mb_music_folder):
    for file in files:
        if file.endswith(('.flac', '.wav', '.mp3', '.WAV', '.Flac', 'MP3', '.FLAC', '.aif', '.m4a')):
            music_files.append(os.path.join(root, file))

for file_path in music_files:
    file = os.path.basename(file_path)

    # tag = TinyTag.get(file_path)
    try:
        tag = TinyTag.get(file_path)
    except Exception as e:
        print(f"Error: {str(e)} - {file_path}")
        continue

    print(f'\n{tag.title}')
    if tag.title:
        artist = tag.artist
        artists = [artist.strip() for artist in re.split(r'[,/]|(?:(?:ft|Ft|Feat|FEAT)\.?)|\&', artist)]
        artist_name = artists[0] if artist else None

        if artist_name:
            artist_name = re.sub(special_characters, '', artist_name)
            
        if artist_name:
            new_file_name = f"{tag.title} - {artist_name}{os.path.splitext(file)[1]}"
        else:
            new_file_name = f"{tag.title}{os.path.splitext(file)[1]}"

    else:
        artist_name = None
        new_file_name = file

    artist_folder = os.path.join(renamed_music_folder, artist_name or "Unknown Title")
    new_file_path = os.path.join(artist_folder, new_file_name)

    if os.path.exists(new_file_path):
        print(f"Alert: File '{new_file_name}' already exists in '{artist_folder}' and won't be moved.")
    else:
        if not os.path.exists(artist_folder):
            os.makedirs(artist_folder)
        shutil.move(file_path, new_file_path)
        print(f"Moved '{file}' to '{artist_folder}'." if tag.title else f"Moved '{file}' to '{artist_folder}'. (Title is unavailable)")

print("\n\nMusic files have been renamed and rearranged successfully!")
print("\nIf folder is not empty, please check the 'Type' of the file!")
