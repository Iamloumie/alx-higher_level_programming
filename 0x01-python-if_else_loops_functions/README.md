# Python and C Programming Project

This project contains a collection of Python and C programs demonstrating various programming concepts and algorithms.

## File Structure

### Python Files

- `0-positive_or_negative.py`: Determines if a number is positive or negative.
- `1-last_digit.py`: Prints the last digit of a number.
- `2-print_alphabet.py`: Prints the alphabet in lowercase.
- `3-print_alphabt.py`: Prints the alphabet in lowercase, excluding 'q' and 'e'.
- `4-print_hexa.py`: Prints numbers from 0 to 98 in decimal and hexadecimal.
- `5-print_comb2.py`: Prints numbers from 0 to 99.
- `6-print_comb3.py`: Prints all possible different combinations of two digits.
- `7-islower.py`: Checks for lowercase character.
- `8-uppercase.py`: Prints a string in uppercase.
- `9-print_last_digit.py`: Prints the last digit of a number.
- `10-add.py`: Adds two integers and returns the result.
- `11-pow.py`: Computes a to the power of b and returns the value.
- `12-fizzbuzz.py`: Prints the numbers from 1 to 100 (FizzBuzz).
- `100-print_tebahpla.py`: Prints the ASCII alphabet in reverse order, alternating lowercase and uppercase.
- `101-remove_char_at.py`: Creates a copy of the string, removing the character at the position n.
- `102-magic_calculation.py`: Python function that does exactly the same as a given Python bytecode.

### C Files

- `13-insert_number.c`: Inserts a number into a sorted singly linked list.
- `13-main.c`: Main file to test the insert_number function.
- `linked_lists.c`: Contains functions for working with linked lists.
- `lists.h`: Header file for the C programs.

### Main Files

- `7-main.py`, `8-main.py`, `9-main.py`, `10-main.py`, `11-main.py`, `12-main.py`, `101-main.py`: Main files to test corresponding Python functions.

## Usage

To run the Python scripts, use the following command:

```
python3 <script_name>.py
```

To compile and run the C programs, use:

```
gcc -Wall -Werror -Wextra -pedantic <c_file_name>.c -o <output_name>
./<output_name>
```

## Notes

- The `__pycache__` directory contains Python 3 bytecode files.
- Make sure you have Python 3 and GCC installed on your system to run these programs.
- Some files might require additional setup or have specific usage instructions. Please refer to the individual file comments for more details.
