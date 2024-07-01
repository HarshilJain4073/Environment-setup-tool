# Environment Setup Script

This Python script automates the setup of directories, environment variables, and configuration files. It utilizes `os`, `argparse`, `shutil`, and `logging` modules.

## Features

- **Directory Creation:**
  - Checks if specified directories exist.
  - Creates directories if they do not exist.
  - Logs creation events and handles errors gracefully.

- **Environment Variable Setup:**
  - Sets environment variables specified in the format `VAR=value`.
  - Logs variable assignments and reports any errors encountered.

- **Configuration File Copy:**
  - Copies configuration files to a specified destination directory.
  - Logs each file copy operation and handles exceptions transparently.

- **Logging:**
  - Configures logging to record setup actions and errors to a specified `setup.log` file.

## Usage

1. **Setup:**
   - Ensure Python 3.x and necessary modules (`os`, `argparse`, `shutil`, `logging`) are installed.

2. **Command Line Arguments:**
   - `--dirs`: List of directories to check/create.
   - `--env`: List of environment variables to set in `VAR=value` format.
   - `--configs`: List of configuration files to copy.
   - `--dest`: Destination directory for configuration files.
   - `--log`: Optional argument to specify the log file name (default: `setup.log`).

3. **Running the Script:**
   - Execute the script with appropriate command line arguments:
     ```bash
     python setup_script.py --dirs /path/to/dir1 /path/to/dir2 --env VAR1=value1 VAR2=value2 --configs /path/to/config1 /path/to/config2 --dest /path/to/destination
     ```

4. **Output:**
   - Displays actions taken (directory creation, environment variable setting, file copying).
   - Logs all operations and errors to `setup.log` for reference.

## Example

Assume the following command sets up directories, and environment variables, and copies configuration files:

  ```bash
  python setup_script.py --dirs /opt/app/logs /opt/app/config --env DEBUG=True VERSION=1.0 --configs /etc/app/config.yaml /etc/app/log.conf --dest /opt/app/config
  ```
    
## Output

```bash
Checking directories...
Directory: /opt/app/logs exists
Directory: /opt/app/config exists
Setting environment variables...
Set environment variable: DEBUG=True Done.
Set environment variable: VERSION=1.0 Done.
Copying configuration files...
Copied /etc/app/config.yaml to /opt/app/config
Copied /etc/app/log.conf to /opt/app/config
Environment setup completed successfully.
```
