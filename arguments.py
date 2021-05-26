#!/usr/bin/env python3

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Get command-line arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-cat',
                        '--read',
                        nargs='*',
                        help='Read a File',
                        metavar='str',
                        type=str)

    parser.add_argument('-touch',
                        '--create',
                        nargs='*',
                        help='Create empty files',
                        metavar='str',
                        type=str)

    parser.add_argument(
        '-cp',
        '--copy',
        nargs='*',
        help=
        'Copy existing files to new existing directory or to become a new file with different name',
        metavar='str',
        type=str)

    parser.add_argument(
        '-mv',
        '--move',
        nargs='*',
        help='Move an existing file to another existing directory',
        metavar='str',
        type=str)

    parser.add_argument('-rm',
                        '--remove',
                        nargs='*',
                        help='Remove an existing file',
                        metavar='str',
                        type=str)

    return parser.parse_args()
