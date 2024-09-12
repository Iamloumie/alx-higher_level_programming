#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg = len(sys.argv)
    if arg == 2:
        print("{} argument:".format(arg - 1))
        for i in range(1, arg):
            print("{}: {}".format(i, sys.argv[i]))
    elif arg > 2:
        print("{} arguments:".format(arg - 1))
        for i in range(1, arg):
            print("{}: {}".format(i, sys.argv[i]))
    elif arg == 1:
        print("0 arguments.")
