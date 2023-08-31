# Rename File Name of Photos and Movies based on Creation Date (EXIF)
Please note that the program may have some **issues** due to my lack of experience.

## Description
This program allows you to rename image files (JPEG, PNG, GIF, NEF RAW) and .MOV video files based on their creation dates. The program uses EXIF data and system metadata to determine the creation date and assigns sequential numbers to the files according to this date.

Examples of renamed files:
- Option 1: `file_0001.png, file_0002.nef`,
- Option 2: `2023-08-31_16-38-11.mov, 2023-06-14_13-39-01.jpg` (EXIF Date Renaming)

## Requirements
- Python 3.x (recommended version 3.6 or newer)
- `Pillow` and `exifread` library
- macOS system (tested on macOS, not tested on Windows)

## Installation

1. Ensure you have the `Pillow` and `exifread` libraries installed:

   ```bash
   pip install Pillow exifread
2. Download the `rename_files.py` file and place it in the directory where your photos and movie files are located.

## Usage
1. Open the Terminal.

2. Navigate to the directory containing the `rename_files.py` file and your photos/movies files:

    ```bash
    cd path/to/your/directory
3. Run the program using the following command:
    ```bash
    python3 rename_files.py
4. The program will ask with option you want to choose. There's two option, you need to specify numer: **1** or **2**
    ```python
    Which renaming option do you choose:

    1. file_0001, file_0002, file_0003...
    2. EXIF Date renaming

    Please choose your number: (1 or 2)
    ```
5. The names of all files in the `source_folder` will be renamed based on their creation dates.

## Process Overview
1. The program scans the designated folder for image files (JPEG, PNG, GIF), .MOV video files, and .NEF RAW image files.

2. For each file:

- If it's a .MOV file, the program retrieves the creation date from system metadata.
- If it's an image file (JPEG, PNG, GIF, or .NEF), the program extracts the creation date from EXIF data.
3. Files are sorted based on their creation dates.

4. Sequential numbers or EXIF date are assigned to files according to their sorting order.

5. File names are modified to the format of ther user's choice.

## Warning
The program automatically renames files in the designated folder. Ensure you run the program in the correct directory and maintain backup copies to prevent data loss.