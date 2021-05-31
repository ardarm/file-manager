#!/usr/bin/env python3

from subprocess import getoutput

prg = "../main.py"
read_options = ['-cat', '--read']


def test_read_first():
    for option in read_options:
        out = getoutput(f"{prg} {option} hello.txt")
        expected = "Hello, friends!"
        assert out.strip() == expected


def test_read_second():
    for option in read_options:
        out = getoutput(f"{prg} {option} hello.txt world.txt")
        expected = """Hello, friends!
World is beautiful,
Enjoy your life!"""
        assert out.strip() == expected

def test_read_third():
    for option in read_options:
        out = getoutput(f"{prg} {option} dummy")
        expected = "dummy is a directory, cannot be read!"
        assert out.strip() == expected

def test_read_fourth():
    for option in read_options:
        out = getoutput(f"{prg} {option} not_exist.txt")
        expected = "not_exist.txt doesn't exist!"
        assert out.strip() == expected
