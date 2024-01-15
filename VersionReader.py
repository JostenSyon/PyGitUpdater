import json
import os

class VersionReader:
    def __init__(self, json_file_path):
        user_profile_name = os.environ['USERNAME']
        self.json_file_path = json_file_path.replace(r'%userprofile%', user_profile_name)

    def get_version(self):
        # Read the JSON file and get the version
        with open(self.json_file_path, 'r') as f:
            config_data = json.load(f)
            version = config_data.get('version', '')
        return version