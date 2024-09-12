#!/usr/bin/python3

# Check if the program runs as main not an import
if __name__ == "__main__":
    from add_0 import add

    # enter the values of the integers a and b
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
