#!/usr/bin/env python3

from arguments import get_args
from operations import (read_files, create_files,
                        copy_files, move_file,
                        remove_file)


def main():
    """Main function"""
    args = get_args()
    files_to_read = args.read
    files_to_create = args.create
    files_to_copy = args.copy
    mv_arg = args.move
    rm_arg = args.remove

    if files_to_read is not None:
        read_files(files_to_read)
    elif files_to_create is not None:
        create_files(files_to_create)
    elif files_to_copy is not None:
        copy_files(files_to_copy)
    elif mv_arg is not None:
        if len(mv_arg) < 2:
            print("\nMust have minimal 2 arguments!")
        else:
            files_to_moved = mv_arg[:len(mv_arg) - 1]
            move_dest = mv_arg[len(mv_arg) - 1]
            for file in files_to_moved:
                move_file(file, move_dest)
    elif rm_arg is not None:
        files_to_removed = rm_arg
        remove_files = [remove_file(file) for file in files_to_removed]
    else:
        print("\nNo arguments provided, please use -h flag to read help")


# --------------------------------------------------

if __name__ == '__main__':
    main()
