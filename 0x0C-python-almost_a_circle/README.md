# Python Geometric Shapes Library

A Python library that implements various geometric shapes with their properties and calculations.
This project includes base shape functionality along with specific implementations for rectangles and squares.

## Project Structure

```
.
├── models/
│   ├── __init__.py
│   ├── base.py
│   ├── rectangle.py
│   └── square.py
└── tests/
    ├── __init__.py
    ├── test_base.py
    ├── test_rectangle.py
    └── test_square.py
```

## Description

This project provides a collection of geometric shape classes with the following components:

- `base.py`: Contains the base shape class with common properties and methods
- `rectangle.py`: Implementation of the Rectangle class
- `square.py`: Implementation of the Square class (inherits from Rectangle)

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <project-directory>
```

## Testing

The project includes a comprehensive test suite for all shape implementations. To run the tests:

```bash
python -m unittest discover tests
```

Test files:

- `test_base.py`: Tests for the base shape functionality
- `test_rectangle.py`: Tests for the Rectangle class
- `test_square.py`: Tests for the Square class

## Usage

```python
from models.rectangle import Rectangle
from models.square import Square

# Create a rectangle
rect = Rectangle(width=5, height=3)
print(f"Rectangle Area: {rect.area()}")

# Create a square
square = Square(side=4)
print(f"Square Area: {square.area()}")
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Run the tests to ensure everything works
5. Commit your changes (`git commit -am 'Add new feature'`)
6. Push to the branch (`git push origin feature/improvement`)
7. Create a Pull Request

## Author

Lawal Adedamola Olumide
