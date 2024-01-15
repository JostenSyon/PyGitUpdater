### PyGitUpdater Class Documentation (Part 1)

#### Overview
The `PyGitUpdater` class is a Python-based updater system designed to manage the update process of an application. It integrates various components such as version checking, downloading, and unpacking to automate the update workflow.

#### Constructor
```python
def __init__(self, config_file_path, force_update):
```
The constructor initializes the `PyGitUpdater` instance with the following parameters:
- `config_file_path`: The path to the configuration file (`config.json`) that contains update-related settings.
- `force_update`: A boolean flag indicating whether to force the update process regardless of the current version.

**Key Operations:**
1. Determines the application path based on whether the application is bundled (using PyInstaller) or not.
2. Copies the `config.json` file to the temporary directory if the application is bundled.
3. Loads the configuration settings from the `config.json` file.
4. Initializes the `force_update` setting based on the command-line argument or the configuration file.
5. Creates instances of `VersionReader`, `RemoteVersionChecker`, and `Downloader` using the configuration settings.

#### Methods
##### terminate_process
```python
def terminate_process(self):
```
The `terminate_process` method terminates a running process specified by its name in the configuration settings. It uses the `subprocess` module to execute the `taskkill` command.

##### start_process
```python
def start_process(self):
```
The `start_process` method starts a new process after a short delay, using the executable name and arguments specified in the configuration settings. It also checks for specific flags in the arguments to determine the update behavior. It uses `subprocess.Popen` to run the process in a non-blocking manner, allowing the updater to continue running.


#### Usage Example
To use the `PyGitUpdater` class, you would first create an instance by providing the path to the `config.json` file and the `force_update` flag. Then, you can call the `terminate_process` and `start_process` methods as needed during the update process.

```python
updater = PyGitUpdater('path/to/config.json', force_update=True)
updater.terminate_process()
# ... perform update tasks ...
updater.start_process()
```

This will terminate the specified process, perform the update tasks, and then start the process with the updated application.



##### update
```python
def update(self):
```
The `update` method orchestrates the entire update process by performing the following steps:
1. Retrieves the local and remote versions of the software.
2. Compares the versions and checks if an update is forced through the configuration.
3. If an update is needed or forced, it prints the available new version and proceeds with the update.
4. Terminates the current running process if necessary.
5. Downloads the new version using the `Downloader` class.
6. Extracts and renames the downloaded files using the `Unpacker` class with a specified prefix and untouch list.
7. Starts the updated process if specified.

#### Command-Line Interface
The class also includes a command-line interface (CLI) for running the updater with the option to force the update. The CLI uses the `argparse` library to parse command-line arguments.

#### Usage Example
To run the `PyGitUpdater` from the command line, you can use the following command:
```shell
python pyGitUpdater.py --force
```
This will force the update process regardless of the current version.

#### Notes
- The `update` method provides informative print statements throughout the process for user feedback.
- The class handles the update process in a way that is transparent to the user, requiring minimal interaction.
- The CLI is a convenient way to integrate the updater into scripts or scheduled tasks.

---

This concludes the documentation for the `PyGitUpdater` class based on the provided code. If you have any more classes or configuration files to document, or if you need further assistance, please let me know.