import os
import time

def watch_directory(directory="."):
    known_files = set(os.listdir(directory))
    while True:
        current_files = set(os.listdir(directory))
        new_files = current_files - known_files
        for file in new_files:
            if file.endswith(".txt"):
                print(f"Detected new file: {file}")
        known_files = current_files
        time.sleep(1)  # Check every second

# Test the function (run and create a .txt file in the directory)
if __name__ == "__main__":
    watch_directory()