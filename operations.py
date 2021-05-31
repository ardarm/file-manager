#!/usr/bin/env python3

import shutil
from pathlib import Path
import os


def read_file(filename):
    try:
        with open(filename) as f:
            print(f.read())
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")
    except IsADirectoryError:
        print(f"\n{filename} is a directory, cannot be read!")


def create_file(filename):
    try:
        Path(filename).touch(exist_ok=False)
        print(f"{filename} created")
    except FileExistsError:
        print(f"{filename} already exist!")


def copy_file(filename, destination):
    try:
        shutil.copy(filename, destination)
        print(f"{filename} copied to {destination}")
    except shutil.SameFileError:
        print(f"\n{filename} already exist!")
    except IsADirectoryError:
        print(f"\n{filename} is a directory, feature will be added soon!")
    except FileNotFoundError:
        print(f"{filename} doesn't exist")


def move_file(filename, destination):
    try:
        shutil.move(filename, destination)
        print(f"{filename} moved to {destination}")
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")


def remove_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} removed!")
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")
