import os
import shutil
from typing import List, Optional
from langchain_core.tools import tool

@tool
def list_files(directory: str = ".") -> str:
    """List files in the given directory."""
    try:
        files = os.listdir(directory)
        return "\n".join(files)
    except Exception as e:
        return f"Error listing files: {str(e)}"

@tool
def read_file(filepath: str) -> str:
    """Read the content of a file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

@tool
def write_file(filepath: str, content: str) -> str:
    """Write content to a file. Overwrites if exists."""
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Successfully wrote to {filepath}"
    except Exception as e:
        return f"Error writing file: {str(e)}"

@tool
def make_directory(directory: str) -> str:
    """Create a new directory."""
    try:
        os.makedirs(directory, exist_ok=True)
        return f"Successfully created directory {directory}"
    except Exception as e:
        return f"Error creating directory: {str(e)}"
