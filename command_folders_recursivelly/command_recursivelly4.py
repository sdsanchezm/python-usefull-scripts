# Simple Script executing recursively commands in a folder

import os

def command_in_folders(initial_folder, command):

    for folder1, subfolders, filenames in os.walk(initial_folder):

        print(f"Executing in folder: {folder1} ")
        os.chdir(folder1)
        os.system(command)


if __name__ == "__main__":
    initial_folder = "./"
    command = "dir"

    command_in_folders(initial_folder, command)
