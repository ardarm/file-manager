#!/usr/bin/env python3

from tkinter import Frame, Button, Listbox


class Interface():
    def __init__(self, window, operations):
        self.window = window
        self.window.title("File Manager")
        self.window.geometry("547x300")

        self.operations = operations

        self.frame_top = Frame(self.window, width=450, height=35,
                               bg='grey').grid(columnspan=8, sticky='we')

        self.button_new_folder = Button(self.frame_top,
                                        width=5,
                                        text='New Folder')
        self.button_new_folder.grid(row=0, column=1, sticky='w', padx=5)
        self.button_new_file = Button(self.frame_top, width=5, text='New File')
        self.button_new_file.grid(row=0, column=2, sticky='w', padx=5)
        self.button_rename = Button(self.frame_top, width=5, text='Rename')
        self.button_rename.grid(row=0, column=3, sticky='w', padx=5)
        self.button_delete = Button(self.frame_top, width=5, text='Delete')
        self.button_delete.grid(row=0, column=4, sticky='w', padx=5)
        self.button_copy = Button(self.frame_top, width=5, text='Copy')
        self.button_copy.grid(row=0, column=5, sticky='w', padx=5)
        self.button_cut = Button(self.frame_top, width=5, text='Cut')
        self.button_cut.grid(row=0, column=6, sticky='w', padx=5)

        self.frame_middle = Frame(self.window)
        self.frame_middle.grid(columnspan=8)

        self.left_listbox = Listbox(self.frame_middle, width=25)
        self.left_listbox.bind('<Double-Button-1>')
        self.left_listbox.grid(row=2, column=0, sticky='w')

        self.right_listbox = Listbox(self.frame_middle, width=25)
        self.right_listbox.bind('<Double-Button-1>')
        self.right_listbox.grid(row=2, column=4, sticky='e')
