#!/usr/bin/python3


"""Defines a text file-reading function."""



def read_file(filename=""):

    """Print the contents of a UTF8 text file to stdout."""

    with open(filename, encoding="utf-8") as f:

        print(f.read(), end="")


0x0B-python-input_output/1-write_file.py


#!/usr/bin/python3


"""Defines a file-writing function."""



def write_file(filename="", text=""):

    """Write a string to a UTF8 text file.

    Args:

        filename (str): The name of the file to write.

        text (str): The text to write to the file.

    Returns:

        The number of characters written.

    """

    with open(filename, "w", encoding="utf-8") as f:

        return f.write(text)
