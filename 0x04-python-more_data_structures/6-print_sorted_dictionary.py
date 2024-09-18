#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for keys in sorted(a_dictionary):
        print(f"{keys}: {a_dictionary[keys]}")
