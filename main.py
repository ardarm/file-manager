#!/usr/bin/env python3

from tkinter import Tk
from interface import Interface
from operations import Operations


def main():
    window = Tk()
    operations = Operations()

    gui = Interface(window, operations)
    operations.get_directory_contents(gui.left_listbox)
    operations.get_directory_contents(gui.right_listbox)

    window.mainloop()


if __name__ == "__main__":
    main()
