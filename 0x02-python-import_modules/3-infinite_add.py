#!/usr/bin/python3

# Adds all command arguments
if __name__ == "__main__":
    import sys

    arg = len(sys.argv)
    count = 0  # initialize the count to zero
    if arg == 1:
        print("0")  # prints zero because there's no argument
    elif arg > 1:
        for i in range(1, arg):
            count = count + int(sys.argv[i])  # sums the whole args
        print("{}".format(count))
