#!/usr/bin/env python3


import urwid
import os

PALETTE = [
    ('reveal focus', 'black', 'dark cyan', 'standout')
   ]

LISTDIR = os.listdir()

class SelectableText(urwid.Text):
    def selectable(self):
        return True

    def keypress(self, size, key):
        return key

def show_or_exit(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

def browse_directory(listdir):
    content = urwid.SimpleListWalker([
        urwid.AttrMap(SelectableText(listdir[i]), '',  'reveal focus') for i in range(len(listdir))
    ])

    content_list = urwid.ListBox(content)
    return content_list

def main():
    loop = urwid.MainLoop(browse_directory(LISTDIR), palette=PALETTE, unhandled_input=show_or_exit)
    loop.run()
    

if __name__ == "__main__":
    main()