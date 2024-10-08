# Python Data Structures Project

This project contains various Python scripts and C programs demonstrating different data structure operations and algorithms.

## Files

### Python Scripts

- `0-print_list_integer.py`: Prints all integers of a list.
- `1-element_at.py`: Retrieves an element from a list.
- `2-replace_in_list.py`: Replaces an element of a list at a specific position.
- `3-print_reversed_list_integer.py`: Prints all integers of a list in reverse order.
- `4-new_in_list.py`: Replaces an element in a list without modifying the original list.
- `5-no_c.py`: Removes all characters 'c' and 'C' from a string.
- `6-print_matrix_integer.py`: Prints a matrix of integers.
- `7-add_tuple.py`: Adds two tuples.
- `8-multiple_returns.py`: Returns a tuple with the length of a string and its first character.
- `9-max_integer.py`: Finds the biggest integer of a list.
- `10-divisible_by_2.py`: Finds all multiples of 2 in a list.
- `11-delete_at.py`: Deletes the item at a specific position in a list.
- `12-switch.py`: Switches the value of two variables.

### C Programs

- `13-is_palindrome.c`: Checks if a singly linked list is a palindrome.
- `linked_lists.c`: Helper functions for linked list operations.

### Header File

- `lists.h`: Header file containing function prototypes and struct definitions.

### Main Files

- Various `*-main.py` and `*-main.c` files: Test the functionality of their corresponding scripts.

## Usage

To run the Python scripts, use the following command:

```
python3 <script_name>.py
```

For C programs, compile using:

```
gcc -Wall -Werror -Wextra -pedantic *.c -o <output_name>
```

Then run the compiled program:

```
./<output_name>
```

## Note

The `__pycache__` directory contains bytecode files generated by Python. It's usually not necessary to interact with these files directly.
