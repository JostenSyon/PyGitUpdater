import os
import requests
import zipfile

class Downloader:
    def __init__(self, url_release, direct_download=False, download_path=None, extract=False, prefix=None):
        self.url_release = url_release
        self.direct_download = direct_download
        self.download_path = download_path if download_path else os.getcwd()
        self.extract = extract
        self.prefix = prefix if prefix else ''

    def download_file(self):
        # Get the JSON data from the URL
        response = requests.get(self.url_release)

        # Check if the request was successful
        if response.status_code != 200:
           print(f"Failed to get data from {self.url_release}. HTTP status code: {response.status_code}")
           return

        data = response.json()

        # Get the download URL
        download_url = data['assets'][0]['browser_download_url']

        # Get the file size in MB
        file_size = data['assets'][0]['size'] / (1024 * 1024)

        # Get the file name
        file_name = os.path.basename(download_url)

        # Display the file name and size
        print(f"The file name is {file_name} and its size is {file_size:.2f} MB.")

        if not self.direct_download:
            print("Do you want to download it? (yes/no)")
            RES = input()
            if RES.lower() not in ["yes", "y"]:
                print("Download cancelled.")
                return

        # Download the file
        response = requests.get(download_url)
        with open(os.path.join(self.download_path, file_name), 'wb') as f:
            f.write(response.content)

        print(f"File downloaded to: {os.path.join(self.download_path, file_name)}")

        # If extract is True, extract the file
        if self.extract and file_name.endswith('.zip'):
            self.extract_and_rename(file_name)

    def extract_and_rename(self, file_name):
        # Construct the full path of the zip file
        zip_path = os.path.join(self.download_path, file_name)

        # Open the zip file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Extract all files
            zip_ref.extractall(self.download_path)

        # Delete the zip file
        os.remove(zip_path)

        # Rename all extracted files
        for fl in os.listdir(self.download_path):
            os.rename(os.path.join(self.download_path, fl), os.path.join(self.download_path, self.prefix + fl))

# Usage
            
# Create an instance of the class
# url_release is the URL of the release you want to download
# direct_download if set to True, the user will not be asked for confirmation before downloading
# download_path is the path where the downloaded file will be saved
# extract if set to True, the downloaded file will be extracted if it's a zip file
# prefix is set to 'new_', so all extracted files will be renamed with this prefix
            
#downloader = Downloader(url_release="https://github.com/user/repo/releases/latest", 
#                        direct_download=True, 
#                        download_path="/path/to/download/directory", 
#                        extract=True, 
#                        prefix="new_")

# Call the download_file method to start the download
#downloader.download_file()

