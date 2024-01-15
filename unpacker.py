import os
import shutil
import zipfile

class Unpacker:
    def __init__(self, download_path, prefix='', untouch=[]):
        self.download_path = download_path
        self.prefix = prefix
        self.untouch = untouch

    def extract_and_rename(self, file_path):
        # Create a temporary directory to extract files
        temp_dir = os.path.join(self.download_path, "temp")
        os.makedirs(temp_dir, exist_ok=True)

        # Open the zip file
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            # Extract all files to the temporary directory
            for entry in zip_ref.infolist():
                zip_ref.extract(entry.filename, temp_dir)

        # Delete the zip file
        os.remove(file_path)

        # Recursive function to move and rename files
        def move_files(directory):
            for name in os.listdir(directory):
                old_path = os.path.join(directory, name)
                if os.path.isfile(old_path):
                    # Check if the file is in the 'untouch' list
                    print(name)
                    if name in self.untouch:
                        new_path = os.path.join(self.download_path, name)
                    else:
                        new_path = os.path.join(self.download_path, self.prefix + name)
                    if os.path.exists(new_path):
                        os.remove(new_path)  # remove the file if it already exists
                    os.rename(old_path, new_path)
                else:
                    move_files(old_path)

        # Call the recursive function
        move_files(temp_dir)

        # Recursive function to remove empty directories
        def remove_empty_dirs(directory):
            if not os.listdir(directory):
                os.rmdir(directory)
            else:
                for name in os.listdir(directory):
                    path = os.path.join(directory, name)
                    if os.path.isdir(path):
                        remove_empty_dirs(path)

        # Call the recursive function
        remove_empty_dirs(temp_dir)
        
        # Remove the "temp" directory and all its contents if it exists
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
