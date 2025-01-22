def read_file_to_string(file_path):
    """
    Reads the content of a file and returns it as a string.

    Args:
      file_path (str): The path to the file to be read.

    Returns:
      str: The content of the file as a string.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content
