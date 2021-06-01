#!/usr/bin/env python3

import shutil
from pathlib import Path
import os


def _read_file(filename):
    try:
        with open(filename) as f:
            print(f.read())
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")
    except IsADirectoryError:
        print(f"\n{filename} is a directory, cannot be read!")


def read_files(files):
    for file in files:
        _read_file(file)


def _create_file(filename):
    try:
        Path(filename).touch(exist_ok=False)
        print(f"{filename} created")
    except FileExistsError:
        print(f"{filename} already exist!")


def create_files(files):
    for file in files:
        _create_file(file)


def _copy_file(filename, destination):
    try:
        shutil.copy(filename, destination)
        print(f"{filename} copied to {destination}")
    except shutil.SameFileError:
        print(f"\n{filename} already exist!")
    except IsADirectoryError:
        print(f"\n{filename} is a directory, feature will be added soon!")
    except FileNotFoundError:
        print(f"{filename} doesn't exist")


def copy_files(files):
    if len(files) < 2:
        raise ValueError("\nCommand must have minimal 2 arguments")
    *filenames, destination = files
    for filename in filenames:
        _copy_file(filename, destination)


def _move_file(filename, destination):
    try:
        shutil.move(filename, destination)
        print(f"{filename} moved to {destination}")
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")


def move_files(files):
    if len(files) < 2:
        raise ValueError("\nCommand must have minimal 2 arguments")
    *filenames, destination = files
    for filename in filenames:
        _move_file(filename, destination)


def _remove_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} removed!")
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")


def remove_files(files):
    for file in files:
        _remove_file(file)
