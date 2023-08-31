
import os
import subprocess

COMMAND_EXEC = 'echo $null >> a.txt'

def command_folder_exec(root_folder):

    for folder, subfolders, filenames in os.walk(root_folder):
        for subfolder in subfolders:

            folder_path = os.path.join(folder, subfolder)

            print(f"Executing command: {COMMAND_EXEC} in folder: {folder_path}")
            
            try:
                subprocess.run(COMMAND_EXEC, shell=True, cwd=folder_path, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error in folder: {folder_path}")
                print(e)


if __name__ == "__main__":

    ACTUAL_FOLDER = './'
    command_folder_exec(ACTUAL_FOLDER)

