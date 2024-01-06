# Downloader Class API

## Class Initialization

```python
downloader = Downloader(url_release, direct_download=False, download_path=None, extract=False, prefix=None)
```


### Parameters

- `url_release` (str): The URL of the release you want to download.
- `direct_download` (bool, optional): If set to True, the user will not be asked for confirmation before downloading. Defaults to False.
- `download_path` (str, optional): The path where the downloaded file will be saved. Defaults to the current working directory.
- `extract` (bool, optional): If set to True, the downloaded file will be extracted if it's a zip file. Defaults to False.
- `prefix` (str, optional): All extracted files will be renamed with this prefix. Defaults to an empty string.

## Methods

### download_file

```python
downloader.download_file()
```

Downloads the file from the `url_release` specified during class initialization. If `direct_download` is True, the file will be downloaded without asking for user confirmation. If `extract` is True and the downloaded file is a zip file, the file will be extracted and all extracted files will be renamed with the `prefix`.

### extract_and_rename

```python
downloader.extract_and_rename(file_name)
```

Extracts all files from a zip file and renames them with the `prefix`. This method is called by `download_file` if `extract` is True.

#### Parameters

- `file_name` (str): The name of the zip file to extract.




#### Example


```python
# Import the class
from Downloader import Downloader

# Create an instance of the class
# url_release is the URL of the release you want to download
# direct_download is set to True, so the user will not be asked for confirmation before downloading
# download_path is the path where the downloaded file will be saved
# extract is set to True, so the downloaded file will be extracted if it's a zip file
# prefix is set to 'new_', so all extracted files will be renamed with this prefix
downloader = Downloader(url_release="https://github.com/user/repo/releases/latest", 
                        direct_download=True, 
                        download_path="/path/to/download/directory", 
                        extract=True, 
                        prefix="new_")

# Call the download_file method to start the download
downloader.download_file()
```