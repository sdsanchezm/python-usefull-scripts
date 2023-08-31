# Pull all repositories in folders recursively with colors
# this script uses subprocess and not the regular os.system method

import os
import subprocess
from colorama import init, Fore


def git_pull_in_folders(path_folder):

    init(autoreset=True)

    for folder_name in os.listdir( path_folder ):

        folder_path = os.path.join(path_folder, folder_name)

        if os.path.isdir( folder_path ):
            print(Fore.YELLOW + f"Pulling changes in repository: {folder_name}")
            try:
                subprocess.run(['git', 'pull'], cwd=folder_path, check=True)
                print(Fore.GREEN + f"git pull completed in folder: {folder_name} ...")
            except subprocess.CalledProcessError:
                print(Fore.RED + f"pull process failed in folder: {folder_name} ...")


if __name__ == "__main__":

    folder_path = './'
    git_pull_in_folders(folder_path)
