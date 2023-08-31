import os
from colorama import init, Fore

def execute_command_in_folders(initial_folder, command):
    
    init(autoreset=True)
    
    for foldername, subfolders, filenames in os.walk(initial_folder):
        print(Fore.BLUE + f"Entering folder: {foldername}")
        print(Fore.MAGENTA + f"Subfolders: {subfolders}")
        for subdir in subfolders:
            actual_folder = os.path.join(foldername, subdir)
            if not os.path.isdir(actual_folder):
                print(Fore.RED + f"Skipping non-existing folder: {actual_folder}")
                continue
            
            print(Fore.YELLOW + f"Executing in folder: {subdir}")
            os.chdir(actual_folder)
            os.system(command)
            
        os.chdir(initial_folder)

if __name__ == "__main__":
    initial_folder = "./"
    command_to_execute = "echo $null > b.txt"

    execute_command_in_folders(initial_folder, command_to_execute)
