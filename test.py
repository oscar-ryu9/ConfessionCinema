import os

def file_exists(file_path):
    return os.path.exists(file_path)

# Example usage
file_path = "E:\Projects\BRAINROT\ConfessionCinema\one.mp3"
if file_exists(file_path):
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' does not exist.")