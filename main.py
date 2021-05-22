#!/usr/bin/env python3


import urwid
import os

class SelectableText(urwid.Text):
    def selectable(self):
        return True

    def keypress(self, size, key):
        return key

    def show_or_exit(key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

listdir = os.listdir()

content = urwid.SimpleListWalker([
    urwid.AttrMap(SelectableText(listdir[i]), '',  'reveal focus') for i in range(len(listdir))
])

listbox = urwid.ListBox(content)

palette = [
    ('reveal focus', 'black', 'dark cyan', 'standout')
   ]

loop = urwid.MainLoop(listbox, palette=palette, unhandled_input=SelectableText.show_or_exit)
loop.run()
