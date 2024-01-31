import os
import glob
import argparse
import json

# The path to start pulling ".java" files from.
lib_folder_path: str = None

# The path for where to generate the resulting ".md" markdown files.
markdown_output_path: str = None

# The path that stores all the files for handwritten documentation.
handwritten_docs_folder_path: str = None

# Config file (default name and location)
config_file_location = "generate_config.json"

# Json file contents that are required to make this project run.
DEFAULT_CONFIG_INFO: str = """
{
    "lib_folder_path":              ".",
    "markdown_output_path":         "out",
    "handwritten_docs_folder_path": "."
}
""";    

if not os.path.exists(config_file_location):
    print("Creating New Config File...")
    with open(config_file_location, "w") as f:
        f.write(DEFAULT_CONFIG_INFO.strip())

# Quick little argument parser
argument_parser = argparse.ArgumentParser(description="A python script to parse java files in team 1816's lib folder.")

argument_parser.add_argument("-cf", "--config_file", required=False, help="The path for a configuration json file.")
argument_parser.add_argument("--generate_default_config", required=False, action="store_true", help="A little helper to quickly generate a default config file. Does not run the rest of the program.")

args = argument_parser.parse_args()

if args.generate_default_config is not None and args.generate_default_config:
    print("Creating Default Config File...")
    with open("default_config.json", "w") as f:
        f.write(DEFAULT_CONFIG_INFO.strip())
    
    exit()

if args.config_file is not None:
    config_file_location = args.config_file

# Get all the config data out of our json file.
try:
    with open(config_file_location) as f:
        config = json.load(f)
        
        lib_folder_path = config['lib_folder_path']
        markdown_output_path = config['markdown_output_path']
        handwritten_docs_folder_path = config['handwritten_docs_folder_path']
        
        print("this is what config contains:", config)
except:
    print(f"Unable to read configuration file at \"{config_file_location}\". \nIt could've been a file type that wasn't json, wasn't correctly configured, or doesn't exist.")
    exit()

if not os.path.exists(markdown_output_path):
    os.makedirs(markdown_output_path)

# Variables to store what files to process
# file_path -> file object

java_files: map = {}
handwritten_files: map = {}



