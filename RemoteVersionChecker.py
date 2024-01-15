import requests
import json

class RemoteVersionChecker:
    def __init__(self, github_url, prefix=None):
        self.github_url = github_url
        self.prefix = prefix

    def get_version(self):
        # Get the latest version available
        response = requests.get(self.github_url)
        data = json.loads(response.text)
        remote = data['tag_name']
        if self.prefix:
            remote = remote.lstrip(self.prefix)  # Remove the prefix
        return remote
