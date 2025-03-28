import os 
import sys

def get_subdirectories(directory_path):
    """
    Returns a list of all subdirectory names in the specified directory.
    """
    # Check if the path exists and is a directory
    if not os.path.isdir(directory_path):
        raise ValueError(f"{directory_path} is not a valid directory")
    
    # Get all subdirectories
    subdirectories = [item for item in os.listdir(directory_path) 
                     if os.path.isdir(os.path.join(directory_path, item))]
    
    return subdirectories
