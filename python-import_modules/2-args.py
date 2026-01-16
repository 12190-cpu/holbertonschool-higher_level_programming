#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1  # on ne compte pas le nom du script

    if argc == 0:
        print("0 arguments.")
    else:
        print(f"{argc} argument{'s' if argc > 1 else ''}:")
        for i in range(1, len(argv)):
            print(f"{i}: {argv[i]}")
