#!/usr/bin/env python3

import os
from tkinter import END


class Operations():
    def __init__(self):
        self.current_directory = os.getcwd()
        self.left_listbox = os.getcwd()
        self.right_listbox = os.getcwd()

    def get_directory_contents(self, listbox):
        self.listbox = listbox
        self.current_directory = self.get_listbox()
        self.listbox.delete(0, END)
        for self.current, self.directories, self.files in os.walk(
                self.current_directory):
            self.listbox.insert(END, '..')
            for directory in self.directories:
                self.listbox.insert(END, directory)
            for file in self.files:
                self.listbox.insert(END, file)
            break

    def get_listbox(self):
        if str(self.listbox)[-1] == "2":
            self.current_directory = self.right_listbox
            return self.right_listbox
        else:
            self.current_directory = self.left_listbox
            return self.left_listbox
