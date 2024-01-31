import os
import glob

# The path to start pulling ".java" files from.
relative_path_for_lib: str = None

# The path for where to generate the resulting ".md" markdown files.
output_path: str = None

# The path that stores all the files for handwritten documentation.
path_for_handwritten_docs: str = None

# Config file
config_file_location = "config.txt"

DEFAULT_CONFIG_INFO: str = """
    relative_path_for_lib: "." # Your relative path
    output_path: "." # Output path for markdown files
    path_for_handwritten_docs: "." # Path for handwritten docs.
""";    

if not os.path.exists(config_file_location):
    with open(config_file_location, "w") as f:
        f.write(DEFAULT_CONFIG_INFO.strip().replace("    ", ""))



