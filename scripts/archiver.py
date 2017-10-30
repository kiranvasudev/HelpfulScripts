#!/usr/bin/env python
"""Script that archives all files and folders in the current working directory"""

import os
import zipfile

__author__ = "Kiran Vasudev"

def recursive_archive(directory, archive_name):
    '''
    Recursively write contents in the current working directory into a zip file
    '''

    # work with all the files and folders in the current dir
    all_Files_and_Folders = [ item for item in os.listdir(directory) if item != archive_name+".zip" ]

    # iterate through all files and folders
    # if folder then call function again
    # if file, write to archive
    for item in all_Files_and_Folders:
        full_path = os.path.join(directory, item)
        if os.path.isfile(full_path):
            archive.write(full_path.split(archive_name)[-1][1:])

        elif os.path.isdir(full_path):
            recursive_archive(full_path, archive_name)


current_dir = os.getcwd()
# Name of the archive is the same as the parent folder
archive_name = current_dir.split("/")[-1]

# Removes the archive with the same name if it already exists in the same directory
if archive_name+".zip" in os.listdir(current_dir):
    os.remove(archive_name+".zip")
    print "Archive already exists. File removed."
    print "Creating new archive now..."

archive = zipfile.ZipFile(archive_name+".zip", 'w', compression=zipfile.ZIP_DEFLATED)

recursive_archive(current_dir, archive_name)

archive.close()
print "Archive has been created"
