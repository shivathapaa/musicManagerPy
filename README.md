# Music File Manager

This script is designed to help you rename and organize your music files in a specified directory. It uses the TinyTag library to read metadata from music files and then rearranges them into artist-specific folders with cleaner filenames. The script focuses on files with extensions like .flac, .wav, .mp3, .aif, and .m4a.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python: The script is written in Python, so you need to have Python installed on your system.

- TinyTag: The script utilizes the TinyTag library to read the metadata from the music files. Install it using the following command:

```bash
pip install tinytag
```

## How to Use

1. **Clone the repository**: Start by cloning this repository to your local machine.

2. **Prepare your music files**: Place your music files in the 'mbMusic' folder. Supported file formats include .flac, .wav, .mp3, .aif, and .m4a.

3. **Run the script**: Execute the script using the following command:

```bash
python musicFileManager.py
```

4. **Sit back and relax**: The script will go through each music file in the 'mbMusic' folder, extract the metadata, and organize them into artist-specific folders with cleaner filenames.

## Renaming and Organizing Process

1. The script first searches for all supported music files (specified extensions) inside the 'mbMusic' folder and its subdirectories.

2. For each music file, it reads its metadata (title and artist) using TinyTag.

3. If the metadata contains a title, the script proceeds to extract the primary artist's name (ignoring features and collaborations) and removes any special characters from it.

4. The script then renames the music file with the format: "Title - Artist.ext". If the artist information is missing, it renames the file as "Title.ext".

5. The script creates an artist-specific folder (or an "Unknown Title" folder if artist information is not available) in the 'managedMusic' directory.

6. The renamed music file is moved to the respective artist folder in the 'managedMusic' directory.

7. If a file with the same name already exists in the destination folder, the script alerts you and skips moving the file.

## Important Notes

- If the script encounters an error while reading the metadata from a music file, it will print an error message along with the file path and continue to the next file.

- After the script completes, check the 'Type' of any files left in the 'mbMusic' folder. These files might not have been supported by the script and need manual processing.

## Example

Let's say you have the following music file in the 'mbMusic' folder:

```
Artist: John Doe
Title: Beautiful Song
File Name: beautiful_song.mp3
```

After running the script, the file will be moved and renamed as follows:

```
Destination Folder: ./managedMusic/John Doe/
Renamed File: Beautiful Song - John Doe.mp3
```

If the title and artist is missing:

```
File Name: something.mp3
```

The script will move the file to the 'Unknown Artist' folder without changing its name.

```
Destination Folder: ./managedMusic/Unknown Artist/
Renamed File: something.mp3          //original file name
```

## Caution

- Before running the script, make sure you have backed up your original music files. Although the script aims to organize the files, it involves renaming and moving, which could lead to data loss if used incorrectly.

- Only run this script on a dedicated directory containing music files that you wish to organize. Using it on other folders might lead to unexpected results.

## Conclusion

Also, you can use separateMp3Files.py for separating music files with a different extension.

With these scripts, you can easily organize and rename your music files based on their metadata, creating a clean and structured music library. Enjoy your music!

---
