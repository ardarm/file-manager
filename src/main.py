#!/usr/bin/env python3

from arguments import get_args
from operations import (read_files, create_files, copy_files, move_files,
                        remove_files)


def main():
    """Main function"""

    args = get_args()
    files_to_read = args.read
    files_to_create = args.create
    files_to_copy = args.copy
    files_to_move = args.move
    files_to_remove = args.remove

    if files_to_read is not None:
        read_files(files_to_read)
    elif files_to_create is not None:
        create_files(files_to_create)
    elif files_to_copy is not None:
        copy_files(files_to_copy)
    elif files_to_move is not None:
        move_files(files_to_move)
    elif files_to_remove is not None:
        remove_files(files_to_remove)
    else:
        print("\nNo arguments provided, please use -h flag to read help")


# --------------------------------------------------

if __name__ == '__main__':
    main()
