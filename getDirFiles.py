"""
Created on Tue Oct  4 13:42:42 2022

@author: carmen
To get and print a directory content
"""

def get_dir_files(address="."):
    import os

    # get the list of all files and directories
    dir_path = address     # current path 
    dir_list = os.listdir(dir_path)

    # list to store files
    res = []

    # print files only
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)

    return res