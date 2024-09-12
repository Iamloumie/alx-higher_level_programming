#!/usr/bin/python3
# import the module named hidden_4
import hidden_4


# define the function 'discover'
def discover():
    # use dir function to the list of attributes in hidden_4
    # assign it to variable 'name'
    name = dir(hidden_4)
    for i in name:
        # check if first two letters are not equal to "__"
        if i[:2] != "__":
            print("{:s}".format(i))


# Check if the script is run as main program not as an import
if __name__ == "__main__":
    discover()  # Calls 'discover' function
