#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_none(self):
        self.assertEqual(max_integer([]), None)

    def test_type(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, -100, "Hello"])

    def test_boolean(self):
        self.assertEqual(max_integer([2, True, False]), 2)

    def test_var_name(self):
        with self.assertRaises(NameError):
            max_integer([a, b])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'a': 2})
