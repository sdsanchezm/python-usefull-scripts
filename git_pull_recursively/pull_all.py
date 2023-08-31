# Script that allows to pull all github repositories in a folder, concurrently
import os
from colorama import init, Fore


def pull_all_folders(folder1):

    for root, directories, files in os.walk(folder1):
        for dir_name in directories:
            folder_path = os.path.join(root, dir_name)

            if os.path.exists(os.path.join(folder_path, '.git')):
                print(Fore.CYAN + f"working folder now: {folder_path} pulling changes now ===========")

                os.system(f"cd {folder_path} && git pull")


if __name__ == "__main__":
    folder1 = "./"
    pull_all_folders(folder1)

