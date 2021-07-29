import os
import shutil
from fastapi import File


def create_folder(folder_name: str) -> bool:
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        return True
    else:
        return False


def clean_workspace(path: str):
    shutil.rmtree(path)


def load_file(file: File, path: str):
    with open(path + file.filename, 'wb') as output:
        contents = file.file.read()
        output.write(contents)


def filename_with_path(file: File, path: str):
    return path + file.filename


def filename_without_extension(filename: str):
    if filename is not None:
        return filename.split('.')[0]


def filename_output_with_path(filename):
    return os.getcwd() + "/output/" + filename


def create_path(foldername):
    return os.getcwd() + "/temp/" + foldername + "/"
