# execute recursively commands in a folder
import os
from colorama import init, Fore

def command_in_folders(initial_folder, command):
    
    init(autoreset=True)
    
    for initial_folder, subfolders, filenames in os.walk(initial_folder):

        print(initial_folder)
        print(subfolders)

        for subdir1 in subfolders:

            print(initial_folder)
            print(subfolders)
            print(Fore.YELLOW + f"Executing in folder: {subdir1}")

            actual_folder = os.path.join(initial_folder, subdir1)

            os.chdir(actual_folder)
            os.system(command)
            # alternative: 
            # os.system(f"cd {subdir1} && echo $null > c.txt")
            # os.system(f"cd ..")

        print(f"initial_folder: {initial_folder}")
        os.chdir(initial_folder)

if __name__ == "__main__":
    initial_folder = "./"
    supercommand1 = "echo $null > b.txt"

    command_in_folders(initial_folder, supercommand1)
