#!/usr/bin/env python3

from tkinter import Frame, Button, Listbox, StringVar, Entry
import os

class Interface():
    def __init__(self, window, operations):
        self.window = window
        self.window.title("PDM File Manager")
        self.window.geometry("547x300")

        self.operations = operations

        self.frame_top = Frame(self.window, width=450, height=35,
                               bg='grey').grid(columnspan=8, sticky='we')

        self.button_new_folder = Button(self.frame_top,
                                        width=5,
                                        text='New Folder',
                                        command=lambda: self.handle_button_click(self.create_directory_trigger))
        self.button_new_folder.grid(row=0, column=1, sticky='w', padx=5)
        self.button_new_file = Button(self.frame_top, width=5, text='New File', command=lambda: self.handle_button_click(self.create_file_trigger))
        self.button_new_file.grid(row=0, column=2, sticky='w', padx=5)
        self.button_rename = Button(self.frame_top, width=5, text='Rename', command=lambda: self.handle_button_click(self.rename_trigger))
        self.button_rename.grid(row=0, column=3, sticky='w', padx=5)
        self.button_delete = Button(self.frame_top, width=5, text='Delete', command=lambda: self.handle_button_click(self.delete_trigger))
        self.button_delete.grid(row=0, column=4, sticky='w', padx=5)
        self.button_copy = Button(self.frame_top, width=5, text='Copy', command=lambda: self.handle_button_click(self.copy_trigger))
        self.button_copy.grid(row=0, column=5, sticky='w', padx=5)
        self.button_cut = Button(self.frame_top, width=5, text='Move', command=lambda: self.handle_button_click(self.move_trigger))
        self.button_cut.grid(row=0, column=6, sticky='w', padx=5)

        self.frame_middle = Frame(self.window)
        self.frame_middle.grid(columnspan=8)

        self.left_listbox = Listbox(self.frame_middle, width=25)
        self.left_listbox.bind('<Double-Button-1>', lambda _: self.handle_item_click(self.left_listbox))
        self.left_listbox.grid(row=2, column=0, sticky='w')

        self.right_listbox = Listbox(self.frame_middle, width=25)
        self.right_listbox.bind('<Double-Button-1>', lambda _: self.handle_item_click(self.right_listbox))
        self.right_listbox.grid(row=2, column=4, sticky='e')

    def handle_button_click(self, trigger):
        if len(self.left_listbox.curselection()) > 0:
            trigger(self.left_listbox, self.right_listbox)
        elif len(self.right_listbox.curselection()) > 0:
            trigger(self.right_listbox, self.right_listbox)

    def handle_item_click(self, listbox):
        self.listbox = listbox
        item = self.operations.get_selected(listbox)
        print(item)
        self.operations.get_directory_contents(listbox)
        self.operations.traverse_directory(item)
        os.chdir(self.operations.current_directory)
        self.operations.get_directory_contents(listbox)

    def get_selected_item(self, listbox):
        idx = listbox.curselection()[0]
        if listbox.get(idx) != '..':
            item = listbox.get(idx)
        return item

    def del_edit_spot(self):
        self.edit_spot.destroy()
        self.button_ok.destroy()
        self.button_cancel.destroy()

    def refresh(self):
        self.operations.get_directory_contents(self.left_listbox)
        self.operations.get_directory_contents(self.right_listbox)

    def create_edit_spot(self, *args):
        item = None
        v = StringVar()
        bottom_frame = Frame(self.window).grid(columnspan=8, sticky='we')
        self.edit_spot = Entry(bottom_frame, textvariable=v, )
        if len(args) == 3:
            item = args[2]
            self.edit_spot.insert(0, item)
        listbox, trigger = args[0], args[1]
        self.edit_spot.grid(row=2, column=2, columnspan=4, padx=50, sticky='e')

        self.button_ok = Button(bottom_frame, text='ok',command=lambda: trigger(listbox, self.edit_spot.get(), self.del_edit_spot, self.refresh, item))
        self.button_ok.grid(row=2, column=4, sticky='e', columnspan=2)
        self.button_cancel = Button(bottom_frame, text='cancel', command=lambda: self.del_edit_spot())
        self.button_cancel.grid(row=2, column=6, sticky='w', columnspan=2)

    def create_file_trigger(self, *args):
        listbox = args[0]
        self.create_edit_spot(listbox, self.operations.create_file)

    def create_directory_trigger(self, *args):
        listbox = args[0]
        self.create_edit_spot(listbox, self.operations.create_directory)

    def rename_trigger(self, *args):
        listbox = args[0]
        item = self.get_selected_item(listbox)
        self.create_edit_spot(listbox, self.operations.rename, item)

    def delete_trigger(self, *args):
        listbox = args[0]
        item = self.get_selected_item(listbox)
        self.operations.delete(item, listbox, self.refresh)

    def copy_trigger(self, *args):
        source, destination = args[0], args[1]
        item = self.get_selected_item(source)
        self.operations.current_directory = self.operations.get_listbox()
        destination = self.operations.current_directory
        self.operations.copy(item, destination, self.refresh)

    def move_trigger(self, *args):
        source, destination = args[0], args[1]
        item = self.get_selected_item(source)
        self.operations.current_directory = self.operations.get_listbox()
        destination = self.operations.current_directory
        self.operations.move(item, destination, self.refresh)
