from systemcommands import *
import os

def file_org_icon():
    print("================================================")
    print("||              FILE ORGANISER                ||")
    owner()
    print("================================================")   

def file_organiser():
    file_org_icon()
    print("================================================")  
    path = input('''||Enter the path of the directory you want to ||
||arrange the files in : ''')
    os.chdir(path)
    files = os.listdir()
    clearscreen()

    for file in files:
        clearscreen()
        if os.path.isfile(file):
            if not os.path.exists("Files"):
                os.mkdir("Files")
                os.rename(file, f'Files/{file}')
                typing('File has been made....\n')
                typing(f'{file} has been moved to Files....\n')
            else:
                os.rename(file, f'Files/{file}')
                typing(f'{file} has been moved to Files....\n')
        else:
            if not os.path.exists("Folders"):
                os.mkdir("Folders")
                os.rename(file, f'Folders/{file}')
                typing('Folder has been made....\n')
                typing(f'{file} has been moved to Folder....\n')
            else:
                os.rename(file, f'Folders/{file}')
                typing(f'{file} has been moved to Folder....\n')
    clearscreen()
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")  
    print("X Files and folders have been arranged successfully X")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")  

file_organiser()