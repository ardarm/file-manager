#!/usr/bin/env python3

import os
from tkinter import END
from pathlib import Path
from shutil import SameFileError, copytree, rmtree, copy, move

from src.operations import list_dir


class Operations():
    def __init__(self):
        self.current_directory = os.getcwd()
        self.left_listbox_path = os.getcwd()
        self.right_listbox_path = os.getcwd()

    def get_listbox(self):
        if str(self.listbox)[-1] == "2":
            self.current_directory = self.right_listbox_path
            return self.right_listbox_path
        else:
            self.current_directory = self.left_listbox_path
            return self.left_listbox_path

    def get_selected(self, listbox):
        print(listbox.curselection())
        i = listbox.curselection()[0]
        print(i)    
        self.selected_item = listbox.get(i)
        return self.selected_item

    def update_listbox_path(self, new_path):
        print(self.listbox)
        if str(self.listbox)[-1] == "2":
            self.right_listbox_path = new_path
            self.current_directory = self.right_listbox_path
            return self.right_listbox_path
        else:
            self.left_listbox_path = new_path
            self.current_directory = self.left_listbox_path
            return self.left_listbox_path

    def _clear_output(self):
        self.listbox.delete(0, END)

    def _list_directory_content(self):
        self._clear_output()
        for item in list_dir(
            self.current_directory
        ):
            self.listbox.insert(END, item)

    def get_directory_contents(self, listbox):
        self.listbox = listbox
        self.current_directory = self.get_listbox()
        self._list_directory_content()

    def traverse_directory(self, item):
        if item == "..":
            new_path = os.path.join(self.current_directory, item)
            new_path = os.path.abspath(new_path)
            self.current_directory = new_path
            self.update_listbox_path(self.current_directory)
        elif os.path.isdir(item):
            new_path = os.path.join(self.current_directory, item)
            self.current_directory = new_path
            self.update_listbox_path(self.current_directory)

    def _create_file(self, filename):
        try:
            Path(filename).touch(exist_ok=False)
            return True
        except FileExistsError:
            print(f'File {filename} already exist!')

    def create_file(self, *args):
        listbox, filename, del_edit_spot, refresh, item = args
        response = self._create_file(filename)
        if response == True:
            del_edit_spot()
            refresh()

    def _create_directory(self, dirname):
        try:
            os.mkdir(dirname)
            return True
        except FileExistsError:
            print(f'Directory {dirname} already exist!')

    def create_directory(self, *args):
        listbox, dirname, del_edit_spot, refresh, item = args
        response = self._create_directory(dirname)
        if response == True:
            del_edit_spot()
            refresh()

    def _rename(self, current_name, new_name):
        if os.path.exists(new_name) and os.path.isfile(new_name):
            return print(f"file {new_name} exist!")
        elif os.path.exists(new_name) and os.path.isdir(new_name):
            return print(f"directory {new_name} exist!")
        else:
            os.rename(current_name, new_name)
            return True
        
    def rename(self, *args):
        listbox, new_name, del_edit_spot, refresh, current_name = args
        self.get_directory_contents(listbox)
        #self.current_directory = self.get_listbox()
        #os.chdir(self.current_directory)
        response = self._rename(current_name, new_name)
        if response == True:
            del_edit_spot()
            refresh()

    def _delete(self, item):
        if os.path.isfile(item):
            os.remove(item)
        elif os.path.isdir(item):
            rmtree(item)
        else:
            print("unknown type")

    def delete(self, item, listbox, refresh):
        #self.get_directory_contents(listbox)
        #self.current_directory = self.get_listbox()
        #os.chdir(self.current_directory)
        print(self.current_directory)
        self._delete(item)
        refresh()

    def _copy_file(self, file, destination):
        try:
            copy(file, destination)
            print(f"{file} copied to {destination}")
        except SameFileError:
            print(f"\n{file} already exist!")

    def _copy_directory(self, directory, destination):
        copytree(directory, destination)

    def copy(self, item, destination, refresh):
        if destination == self.left_listbox_path:
            item_path = os.path.join(self.right_listbox_path, item)
            #os.chdir(self.right_listbox_path)
        else:
            item_path = os.path.join(self.left_listbox_path, item)
            #os.chdir(self.left_listbox_path)
        if os.path.isfile(item_path):
            self._copy_file(item_path, destination)
        elif os.path.isdir(item_path):
            self._copy_directory(item_path, destination)
        else:
            print("unknown type")
        refresh()

    def _move(self, item, destination):
        move(item, destination)
        print(f"{item} moved to {destination}")

    def move(self, item, destination, refresh):
        if destination == self.left_listbox_path:
            item_path = os.path.join(self.right_listbox_path, item)
            #os.chdir(self.right_listbox_path)
        else:
            item_path = os.path.join(self.left_listbox_path, item)
            #os.chdir(self.left_listbox_path)
        self._move(item_path, destination)
        refresh()
