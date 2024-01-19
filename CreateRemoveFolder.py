# Author: Luunahri (https://github.com/Luunahri)

# This program allows you to create and remove folders in a provided path.
# Once you run it and provide the action which you want to do to the switch, 
# it will create the file with the name that you provided, it will open it, and it will create a readme.txt file created alongside it.

# Here we import os and subprocess, which will be necessary for creating, and opening files.
import os   
import subprocess

# Replace "your_folder_path" with the name of your liking, 
# and the path to the folder you wish to create the folders in.
your_folder_path = "C:\\Users\%USER%\Desktop"  

# This function creates a new folder.
def case_createFolder():

    # We create two variables, which will hold both the name, 
    # and the connection between the path and the folder's name.
    folder_name = input("Please provide a folder name: ")
    folder_path = os.path.join(your_folder_path, folder_name)

    # os.makedirs takes the provided path and name and creates the folder.
    os.makedirs(folder_path, exist_ok=True)
    print(f"Folder {folder_path} created successfully!")

    # This function opens the folder in the file explorer. 
    # (the f provided within the brackets is used to tell the function that there is a variable inside the {} brackets)
    subprocess.Popen(f'explorer "{folder_path}"')

    # In this section you must manually put in the path of the main folder followed by the folder's name the user provided earlier, after that we provide the text file's name. 
    # (as for why you can't just put in the "your_folder_path" variable instead of putting it in manually I couldn't figure out on my own, I'm very sorry)
    file = "C:/Users/%USER%/Desktop/" + folder_name + "/readme.txt"

    # In this section we open the text file, and we write "Hello, World!" inside.
    # The "w" within the brackets means that we are writing to the file, you can change it to your liking.
    with open(file, "w") as file:
        file.write("Hello, World!")

    # We close the file.
    file.close()

#This function is the opposite of the previous one, it instead removes the provided folder.
def case_removeFolder():

    print("Folders in directory 'your_path_here(optional)': ")
    print("")

    # We create a list of folders in the provided path.
    folders = [f for f in os.listdir(your_folder_path) if os.path.isdir(os.path.join(your_folder_path, f))]
    for folder in folders:
        print("   ", folder)

    print("")

    # We ask the user which folder they wish to remove.
    folder_name = input("Provide a folder name which you wish to remove: ")
    folder_path = os.path.join(your_folder_path, folder_name)

    # We then remove said folder with the following function:
    os.rmdir(folder_path)
    print(f"Folder {folder_path} removed successfully!")

# !IMPORTANT! We then create a two case switch, which will execute an action depending on the user's input.

switch = {
    "Create": case_createFolder,
    "Remove": case_removeFolder
}

# This action will execute first in the program, as it's not a function unlike the upper part of the code, in here we ask the user about the action they wish to execute.
userAction = input("What would you like to do? (Create, Remove): ")

# The switch then executes a function depending on the user's input.
# In this case it's either "Create" or "Remove"

if "Create" or "Remove" in switch:
    switch[userAction]()
