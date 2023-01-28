import os
from get_images import download_images

def folder_create(images):
    try:
        folder_name = input("\nEnter Folder Name:- ")
        # folder creation
        os.mkdir(folder_name)

    # if folder exists with that name, ask another name
    except:
        print("\nFolder Exist with that name!")
        folder_create()

    # image downloading start
    download_images(images, folder_name)

