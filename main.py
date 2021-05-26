#!/usr/bin/env python3

from arguments import get_args
from operations import *


def main():
    """Main function"""

    args = get_args()
    cat_arg = args.read
    touch_arg = args.create
    cp_arg = args.copy
    mv_arg = args.move
    rm_arg = args.remove

    if cat_arg is not None:
        if len(cat_arg) < 1:
            print("Must have minimal 1 argument")
        else:
            files_to_read = cat_arg
            for file in files_to_read:
                read_file(file)
    elif touch_arg is not None:
        if len(touch_arg) < 1:
            print("Must have minimal 1 argument")
        else:
            files_to_create = touch_arg
            for file in files_to_create:
                create_file(file)
    elif cp_arg is not None:
        if len(cp_arg) < 2:
            print("\nCommand must have minimal 2 arguments")
        else:
            files_to_copy = cp_arg[:len(cp_arg) - 1]
            copy_dest = cp_arg[len(cp_arg) - 1]
            for file in files_to_copy:
                copy_file(file, copy_dest)
    elif mv_arg is not None:
        if len(mv_arg) < 2:
            print("\nMust have minimal 2 arguments!")
        else:
            files_to_moved = mv_arg[:len(mv_arg) - 1]
            move_dest = mv_arg[len(mv_arg) - 1]
            for file in files_to_moved:
                move_file(file, move_dest)
    elif rm_arg is not None:
        if len(rm_arg) < 1:
            print("\nMust have minimal 1 argument")
        else:
            for file in rm_arg:
                remove_file(file)
    else:
        print("\nNo arguments provided, please use -h flag to read help")


# --------------------------------------------------

if __name__ == '__main__':
    main()
