#!/usr/bin/python3

"""Module to test Base class"""

import unittest
from models.base import Base


class test_base(unittest.TestCase):
    """Class to test Base Class"""
    def test_id_none(self):
        """test id"""
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        """test id"""
        b = Base(50)
        self.assertEqual(50, b.id)

    def test_id_zero(self):
        """test id"""
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        """test id"""
        b = Base(-20)
        self.assertEqual(-20, b.id)
