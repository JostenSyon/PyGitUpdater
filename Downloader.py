import os
import requests

from unpacker import Unpacker

class Downloader:
    def __init__(self, url_release, direct_download=False, download_path=None):
        self.url_release = url_release
        self.direct_download = direct_download
        self.download_path = download_path if download_path else os.getcwd()

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

        return os.path.join(self.download_path, file_name)
