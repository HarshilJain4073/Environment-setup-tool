import os
import argparse
import shutil
import logging

def setup_logging(log_file):
    logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s', filename=log_file)

def create_directories(directories):
    logging.info("Checking directories...")
    print("Checking directories...")
    for directory in directories:
        try:
            if os.path.isdir(directory):
                logging.info(f"Directory: {directory} exists")
                print(f"Directory: {directory} exists")
            else:
                os.makedirs(directory)
                logging.info(f"Created directory: {directory}")
                print(f"Created directory: {directory}")
        except Exception as e:
            logging.error(f"Error creating directory {directory}: {e}")
            print(f"Error creating directory {directory}: {e}")


def environment_setup(env_vars):
    logging.info("Setting environment variables...")
    print("Setting environment variables...")
    try:
        for key,value in env_vars.items():
            os.environ[key] = value
            logging.info(f"Set environment variable: {key}={value} Done.")
            print(f"Set environment variable: {key}={value} Done.")
    except Exception as e:
        logging.error(f"Error found: {e}")
        print(f"Error found: {e}")

def copy_configuration_files(config_files, dest_dir):
    logging.info("Copying configuration files...")
    print("Copying configuration files...")
    for config_file in config_files:
        try:
            shutil.copy(config_file, dest_dir)
            logging.info(f"Copied {config_file} to {dest_dir}")
            print(f"Copied {config_file} to {dest_dir}")
        except Exception as e:
            logging.error(f"Error copying file {config_file} to {dest_dir}: {e}")
            print(f"Error copying file {config_file} to {dest_dir}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Environment Setup Script")
    parser.add_argument('--dirs', nargs='+', required=True, help="Directories to create")
    parser.add_argument('--env', nargs='+', required=True, help="Environment variables to set (format: VAR=value)")
    parser.add_argument('--configs', nargs='+', required=True, help="Configuration files to copy")
    parser.add_argument('--dest', required=True, help="Destination directory for configuration files")
    parser.add_argument('--log', default='setup.log', help="Log file")

    args = parser.parse_args()
   
    setup_logging(args.log)

    directories = args.dirs
    env_vars = dict(var.split('=') for var in args.env)
    config_files = args.configs
    dest_dir = args.dest

    create_directories(directories)
    environment_setup(env_vars)
    copy_configuration_files(config_files, dest_dir)
    logging.info(f"Environment setup completed successfully.")
    print(f"Environment setup completed successfully.")

if __name__ == "__main__":
    main()

