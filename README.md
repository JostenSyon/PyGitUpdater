# PyGitUpdater

## Overview
PyGitUpdater is a Python-based tool that automates the update process for applications hosted on GitHub. Originally created to update the GreenLuma Manager fork, it has since become a flexible solution for managing updates across various independent projects.

## Features
- **Automated Update Checks**: Checks for new releases on GitHub.
- **Direct Downloads**: Downloads updates directly if configured, without user prompts.
- **Customizable Configuration**: Allows for detailed settings through a `config.json` file.
- **Command-Line Interface**: Supports command-line arguments to force updates.
- **Versatile Tool**: Adaptable for any GitHub-hosted project.

## Components
PyGitUpdater includes several classes that handle different aspects of the update process:

### VersionReader
Reads the local version of the application from a JSON file and compares it with the remote version available on GitHub.

### RemoteVersionChecker
Checks the remote version of the application using the GitHub API and compares it with the local version.

### Downloader
Downloads the update files from the GitHub release URL and saves them to a specified path.

### Unpacker
Extracts the downloaded files and applies the update, while preserving certain files specified in the `untouch` list.

### PyGitUpdater (Main Class)
Orchestrates the update process by utilizing the other classes, manages the workflow, and provides a command-line interface for advanced operations.

## Usage
To use PyGitUpdater, follow these steps:
1. Set up a `config.json` file with your project's current version and other configurations.
2. Integrate PyGitUpdater into your project's workflow.
3. Run PyGitUpdater to check for and apply updates.

## Getting Started
1. Clone the repository or download the latest release of PyGitUpdater.
2. Customize the `config.json` file according to your project's requirements.
3. Ensure that your GitHub project has releases tagged with version numbers.
4. Integrate PyGitUpdater into your project's update routine.

## Example
Here's a simple example of how to run PyGitUpdater with the force update option:

```bash
python PyGitUpdater.py --force
```

This command will force the update process, bypassing the version check.

## License
PyGitUpdater is released under the MIT License. You are free to use, modify, and distribute it according to the license terms.

## Contributions
Contributions are welcome! If you have any suggestions or improvements, feel free to fork the repository, make your changes, and submit a pull request.

---