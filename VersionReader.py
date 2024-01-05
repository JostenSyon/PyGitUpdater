import json
import os

class VersionReader:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path

    def get_version(self):
        # Read the JSON file and get the version
        with open(self.json_file_path, 'r') as f:
            config_data = json.load(f)
            version = config_data.get('version', '')
        return version

# Usage
    
# Get the username from the environment variables
#user_profile_name = os.environ['USERNAME']
#json_file_path = os.path.join(r"C:\Users", user_profile_name, r"AppData\Local\GLR_Manager\config.json")

# Create a VersionReader instance and print the version
#version_reader = VersionReader(json_file_path)
#print(version_reader.get_version())