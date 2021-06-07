#!/usr/bin/env python3

import os
from tkinter import END

from src.operations import list_dir


class Operations():
    def __init__(self):
        self.current_directory = os.getcwd()
        self.left_listbox = os.getcwd()
        self.right_listbox = os.getcwd()

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

    def get_listbox(self):
        if str(self.listbox)[-1] == "2":
            self.current_directory = self.right_listbox
            return self.right_listbox
        else:
            self.current_directory = self.left_listbox
            return self.left_listbox
