### `config.json` File Documentation

#### Overview
The `config.json` file contains configuration settings for the `PyGitUpdater` system. This file is crucial for directing the updater's behavior during the application's update process.

#### `config.json` File Structure
```json
{
    "json_local_path": "Local path to the config.json file",
    "github_url": "GitHub API URL to check for the latest release",
    "prefix": "Prefix used to identify versions (e.g., 'v' for 'v1.0.0')",
    "direct_download": "Boolean flag to enable direct download without confirmation prompt",
    "force_update": "Boolean flag to force the update regardless of the current version",
    "download_path": "Path where downloaded files are saved during the update",
    "process_name_pre_update": "Name of the process to terminate before starting the update",
    "executable_name_post_update": "Name of the executable to launch after the update",
    "args_post_update": "Arguments to pass to the post-update executable",
    "untouch": "List of files or directories to exclude during the update"
}
```

#### Field Descriptions
- `json_local_path`: Specifies the local path to the `config.json` file. It uses the `%userprofile%` environment variable to refer to the user profile folder.
- `github_url`: The GitHub API URL to fetch information about the latest available release of the software.
- `prefix`: The prefix used to identify software versions. For example, if versions are tagged as 'v1.0.0', the prefix would be 'v'.
- `direct_download`: If set to `true`, the updater will directly download the new version without asking for user confirmation.
- `force_update`: If set to `true`, the updater will force an update even if the current version is up-to-date.
- `download_path`: The path where downloaded files will be saved. If left empty, the updater may use a default or temporary path.
- `process_name_pre_update`: The name of the application's process that needs to be terminated before beginning the update.
- `executable_name_post_update`: The name of the application's executable to launch after the update.
- `args_post_update`: Arguments to pass to the executable after the update. These can include flags to control post-update application behavior.
- `untouch`: A list of files or directories that should not be modified or deleted during the update. This is useful for preserving custom configurations or other important data.

#### Usage Example
To use the `config.json` file with the `PyGitUpdater` class, you would initialize the updater with the path to the configuration file and, if necessary, set the `force_update` flag:

```python
updater = PyGitUpdater('C:\\Users\\%userprofile%\\AppData\\Local\\GLR_Manager\\config.json', force_update=False)
```

After initializing the updater, you can proceed with the update process following the logic defined in your `PyGitUpdater` class.

I hope this documentation is helpful to you! If you need further information or have other parts of the code to document, please feel free to ask.