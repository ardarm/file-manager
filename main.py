#!/usr/bin/env python3

from tkinter import Tk
from interface import Interface
from operations import Operations


def main():
    window = Tk()
    operations = Operations()

    gui = Interface(window, operations)

    window.mainloop()


if __name__ == "__main__":
    main()
