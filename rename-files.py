import os
from datetime import datetime, timezone
from PIL import Image
import exifread


def get_metadata_date_taken_from_movie(file_path):
    try:
        creation_date_str = os.popen(
            f"mdls -name kMDItemContentCreationDate -raw '{file_path}'"
        ).read()
        creation_date = datetime.strptime(
            creation_date_str.strip(), "%Y-%m-%d %H:%M:%S %z"
        )
        return creation_date
    except Exception as e:
        print(f"Error reading creation date: {e}")
    return None


def get_exif_date_taken_from_photos(file_path):
    try:
        with Image.open(file_path) as img:
            exif_data = img._getexif()
            if exif_data and 36867 in exif_data:
                date_taken = exif_data[36867]
                date_taken_utc = datetime.strptime(
                    date_taken, "%Y:%m:%d %H:%M:%S"
                ).replace(tzinfo=timezone.utc)
                return date_taken_utc
    except Exception as e:
        print(f"Error reading EXIF data: {e}")
    return None


def get_nef_date_taken_from_photos(image_path):
    try:
        with open(image_path, "rb") as f:
            tags = exifread.process_file(f, details=False)
            if "Image DateTime" in tags:
                date_taken = tags["Image DateTime"].values
                return datetime.strptime(date_taken, "%Y:%m:%d %H:%M:%S").replace(
                    tzinfo=timezone.utc
                )
    except Exception as e:
        print(f"Error reading NEF data: {e}")
    return None


def rename_files(source_folder):
    index = 1  # Add custom index
    files_to_rename_list = []

    for filename in os.listdir(source_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".mov", ".nef")):
            file_path = os.path.join(source_folder, filename)
            if filename.lower().endswith(".mov"):
                date_taken = get_metadata_date_taken_from_movie(file_path)
            elif filename.lower().endswith(".nef"):
                date_taken = get_nef_date_taken_from_photos(file_path)
            else:
                date_taken = get_exif_date_taken_from_photos(file_path)

            if date_taken:
                files_to_rename_list.append((file_path, date_taken))

    sorted_photos = sorted(files_to_rename_list, key=lambda x: x[1])

    for file_path, _ in sorted_photos:
        extension = os.path.splitext(file_path)[1]
        new_name = (
            f"file_{index:04d}" + extension)  # Change "file" to your custom file name
        new_path = os.path.join(source_folder, new_name)
        os.rename(file_path, new_path)
        print(f"Renamed {os.path.basename(file_path)} to {new_name}")
        index += 1


def main():
    source_folder = "."  # Add a path to the files you want to rename
    rename_files(source_folder)


if __name__ == "__main__":
    main()
