from VersionReader import VersionReader
from RemoteVersionChecker import RemoteVersionChecker
from Downloader import Downloader
import json

class PyGitUpdater:
    def __init__(self, config_file_path):
        with open(config_file_path, 'r') as f:
            self.config = json.load(f)

        self.version_reader = VersionReader(self.config['json_local_path'])
        self.version_checker = RemoteVersionChecker(self.config['github_url'], self.config.get('prefix'))
        self.downloader = Downloader(self.config['github_url'], self.config.get('direct_download'), self.config.get('download_path'))

    def update(self):
        local_version = self.version_reader.get_version()
        remote_version = self.version_checker.get_version()

        if local_version != remote_version:
            print(f"New version {remote_version} is available. Current version is {local_version}.")
            self.downloader.download_file()
        else:
            print("You are up-to-date!")

# Usage
#updater = PyGitUpdater("/path/to/your/config.json")
updater = PyGitUpdater("config.json")            
updater.update()