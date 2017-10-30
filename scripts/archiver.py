#!/usr/bin/env python
"""Script that archives all files and folders in the current working directory"""

import os
import zipfile

__author__ = "Kiran Vasudev"

def recursive_archive(directory, archive_name):
    all_Files_and_Folders = [ item for item in os.listdir(directory) if item != archive_name+".zip" ]

    for item in all_Files_and_Folders:
        full_path = os.path.join(directory, item)
        if os.path.isfile(full_path):
            archive.write(full_path.split(archive_name)[-1][1:])

        elif os.path.isdir(full_path):
            recursive_archive(full_path, archive_name)


current_dir = os.getcwd()
archive_name = current_dir.split("/")[-1]

if archive_name+".zip" in os.listdir(current_dir):
    os.remove(archive_name+".zip")
    print "Archive already exists. File removed."
    print "Creating new archive now..."

archive = zipfile.ZipFile(archive_name+".zip", 'w', compression=zipfile.ZIP_DEFLATED)

recursive_archive(current_dir, archive_name)

archive.close()
print "Archive has been created"
