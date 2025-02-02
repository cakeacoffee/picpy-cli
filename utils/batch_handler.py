import os


def process(
    input_path: str = "images/input", output_path: str = "images/output"
) -> None:
    for filename in os.listdir(input_path):
        print(filename)


# **--- FILE HANDLING ---**


def copy_files(
    input_path: str = "images/input", output_path: str = "images/output"
) -> None:
    """copy files from input directory to output directory"""
    # TODO: implement (keep name and default, by date, by base name and increment)


# **--- FILE DATA ---**


def list_files(
    input_path: str = "images/input",
) -> None:
    """list all files in the given directory"""
    for filename in os.listdir(input_path):
        print(filename)


def count_file_type(
    input_path: str = "images/input",
) -> str:
    """count file type and display and return result"""
    result = ""
    # TODO: implement
    return result


def file_size(
    input_path: str = "images/input",
) -> str:
    """get size for each file and display and return result"""
    return os.stat(input_path).st_size
