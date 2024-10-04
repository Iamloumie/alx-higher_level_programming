# Python Function Test Files

This repository contains a collection of text files and a Python script that are used for testing various Python functions. These files likely contain test cases and expected outputs for corresponding Python functions.

## Files

1. `0-add_integer.txt`: Test cases for an integer addition function.
2. `2-matrix_divided.txt`: Test cases for a matrix division function.
3. `3-say_my_name.txt`: Test cases for a function that prints a name.
4. `4-print_square.txt`: Test cases for a function that prints a square.
5. `5-text_indentation.txt`: Test cases for a text indentation function.
6. `6-max_integer_test.py`: A Python script with unit tests for finding the maximum integer in a list.
7. `100-matrix_mul.txt`: Test cases for a matrix multiplication function.
8. `101-lazy_matrix_mul.txt`: Test cases for an alternative (possibly NumPy-based) matrix multiplication function.

## Purpose

These files are designed to test the functionality and edge cases of various Python functions. They likely contain:

- Input values
- Expected output
- Edge cases
- Error scenarios

The `.txt` files are probably meant to be used with Python's `doctest` module, which allows for easy integration of tests in documentation.

## Usage

### For .txt files

To run tests using the `doctest` module, you can use the following command in your terminal:

```
python -m doctest -v [filename].txt
```

Replace `[filename]` with the name of the text file you want to test.

### For 6-max_integer_test.py

This file likely contains unit tests using Python's `unittest` module. To run these tests, use:

```
python 6-max_integer_test.py
```

## Requirements

- Python 3.x
- The corresponding Python functions that these files are designed to test (not included in this list)
