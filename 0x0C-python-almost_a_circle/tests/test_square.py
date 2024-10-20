#!/usr/bin/python3

"""Module for testing square class"""

from io import StringIO
import sys
import unittest
from models.square import Square


class SquareTests(unittest.TestCase):
    """Tests for Square class."""
    def setUp(self):
        self.sqr = Square(15, 0, 0)

    def test_size(self):
        """Testing height"""
        self.assertEqual(self.sqr.size, 15)

    def test_x_val(self):
        """testing the x value"""
        self.sqr.x = 0
        self.assertEqual(self.sqr.x, 0)

    def test_y_val(self):
        """testing the x value"""
        self.sqr.y = 0
        self.assertEqual(self.sqr.y, 0)

    def test_x_neg(self):
        """testing assigning neg to x"""
        with self.assertRaises(ValueError):
            self.sqr.x = -1

    def test_y_neg(self):
        """testing assigning neg to y"""
        with self.assertRaises(ValueError):
            self.sqr.y = -1

    def test_width_zero(self):
        """testing assigning 0 to width"""
        with self.assertRaises(ValueError):
            self.sqr.width = 0

    def test_height_zero(self):
        """testing assigning 0 to height"""
        with self.assertRaises(ValueError):
            self.sqr.height = 0

    def test_string_assign_width(self):
        """test assigning string to width"""
        with self.assertRaises(TypeError):
            self.sqr.width = "4"

    def test_string_assign_height(self):
        """test assigning string to height"""
        with self.assertRaises(TypeError):
            self.sqr.height = "4"

    def test_bool_assign_width(self):
        """test assigning bool to width"""
        with self.assertRaises(TypeError):
            self.sqr.width = True

    def test_bool_assign_height(self):
        """test assigning bool to height"""
        with self.assertRaises(TypeError):
            self.sqr.height = True

    def test_none_assign_width(self):
        """test assigning None to width"""
        with self.assertRaises(TypeError):
            self.sqr.width = None

    def test_none_assign_height(self):
        """test assigning None to height"""
        with self.assertRaises(TypeError):
            self.sqr.height = None

    def test_float_assign_width(self):
        """testing assigning float value to width"""
        with self.assertRaises(TypeError):
            self.sqr.width = 7.8

    def test_float_assign_height(self):
        """testing assigning float value to height"""
        with self.assertRaises(TypeError):
            self.sqr.height = 7.8

    def test_list_assign_width(self):
        """testing assigning float value to width"""
        with self.assertRaises(TypeError):
            self.sqr.width = [8, 9]

    def test_list_assign_height(self):
        """testing assigning float value to height"""
        with self.assertRaises(TypeError):
            self.sqr.height = [8, 9]

    def test_string_assign_x(self):
        """test assigning string to x"""
        with self.assertRaises(TypeError):
            self.sqr.x = "4"

    def test_string_assign_y(self):
        """test assigning string to y"""
        with self.assertRaises(TypeError):
            self.sqr.y = "4"

    def test_bool_assign_x(self):
        """test assigning bool to x"""
        with self.assertRaises(TypeError):
            self.sqr.x = True

    def test_bool_assign_y(self):
        """test assigning bool to y"""
        with self.assertRaises(TypeError):
            self.sqr.y = True

    def test_none_assign_x(self):
        """test assigning None to x"""
        with self.assertRaises(TypeError):
            self.sqr.x = None

    def test_none_assign_y(self):
        """test assigning None to y"""
        with self.assertRaises(TypeError):
            self.sqr.y = None

    def test_float_assign_x(self):
        """testing assigning float value to x"""
        with self.assertRaises(TypeError):
            self.sqr.x = 7.8

    def test_float_assign_y(self):
        """testing assigning float value to y"""
        with self.assertRaises(TypeError):
            self.sqr.y = 7.8

    def test_list_assign_x(self):
        """testing assigning float value to x"""
        with self.assertRaises(TypeError):
            self.sqr.x = [8, 9]

    def test_list_assign_y(self):
        """testing assigning float value to y"""
        with self.assertRaises(TypeError):
            self.sqr.y = [8, 9]

    def test_id(self):
        """test checking id"""
        r = Square(1, 2, 3, 4)
        self.assertEqual(r.id, 4)

    def test_area(self):
        """testing area"""
        self.assertEqual(self.sqr.area(), self.sqr.height * self.sqr.width)

    def test_normal_update(self):
        """normal testing of the update function"""
        self.sqr.update(12, 67, 22, 1)
        self.assertEqual(self.sqr.id, 12)
        self.assertEqual(self.sqr.size, 67)
        self.assertEqual(self.sqr.x, 22)
        self.assertEqual(self.sqr.y, 1)

    def test_id_update(self):
        """updating the id using update"""
        self.sqr.update(77)
        self.assertEqual(self.sqr.id, 77)

    def test_string_id_update(self):
        """updating the id using update"""
        with self.assertRaises(TypeError):
            self.sqr.update("77")

    def test_list_id_update(self):
        """test to assigning list to update"""
        with self.assertRaises(TypeError):
            self.sqr.update([1, 2, 3, 4])

    def test_float_id_update(self):
        """test to assigning float to update"""
        with self.assertRaises(TypeError):
            self.sqr.update(8.9)

    def test_str_str_update(self):
        """test assigning string to update"""
        with self.assertRaises(TypeError):
            self.sqr.update(69, "haha", "nice")

    def test_overload_update(self):
        """test passing more than 5 values to update"""
        with self.assertRaises(IndexError):
            self.sqr.update(12, 67, 22, 1, 9, 234, 12, 395, 45945)

    def test_kwargs_update(self):
        """test to check the kwargs values are assigned"""
        self.sqr.update(y=54, size=65, x=12, id=89)
        self.assertEqual(self.sqr.id, 89)
        self.assertEqual(self.sqr.size, 65)
        self.assertEqual(self.sqr.x, 12)
        self.assertEqual(self.sqr.y, 54)

    def test_kwargs_args_update(self):
        """test to put kwargs and args together"""
        self.sqr.update(1, 2, 3, id=45)
        self.assertEqual(self.sqr.id, 1)
        self.assertEqual(self.sqr.size, 2)
        self.assertEqual(self.sqr.x, 3)

    def test_str_overload(self):
        """test for string overload"""
        self.sqr.update(1, 2, 3, 4)
        self.assertEqual(self.sqr.__str__(), "[Square] (1) 3/4 - 2")

    def test_negative_width(self):
        """Test assigning a negative width value."""
        with self.assertRaises(ValueError):
            self.sqr.width = -5

    def test_negative_height(self):
        """Test assigning a negative height value."""
        with self.assertRaises(ValueError):
            self.sqr.height = -5

    def test_area_after_attribute_change(self):
        """Test area is correctly updated after changing width and height."""
        self.sqr.width = 10
        self.sqr.height = 5
        self.assertEqual(self.sqr.area(), 50)

    def tearDown(self):
        del self.sqr


class TestSquareDisplay(unittest.TestCase):
    """Class for testing square display"""
    def setUp(self):
        """Redisqr stdout to capture the printed output"""
        self.saved_stdout = sys.stdout
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        """Restore the original stdout"""
        sys.stdout = self.saved_stdout

    def test_display_no_offset(self):
        """tesing no display offset"""
        s = Square(3, 2)
        s.display()
        expected_output = "  ###\n  ###\n  ###\n"
        self.assertEqual(self.output.getvalue(), expected_output)

    def test_display_with_offset(self):
        """testing display offset"""
        s = Square(3, 2, 2, 1)
        s.display()
        expected_output = "\n\n  ###\n  ###\n  ###\n"
        self.assertEqual(self.output.getvalue(), expected_output)

    def test_display_empty_sqrangle(self):
        """testing empty square"""
        with self.assertRaises(ValueError):
            s = Square(0, 0)
            s.display()


if __name__ == "__main__":
    unittest.main()
