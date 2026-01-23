 #!/usr/bin/python3
"""Unittests for max_integer([..])

This module contains a class with unittests for the function max_integer.
It tests normal cases, edge cases, and error handling.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer function."""

    def test_ordered_list(self):
        """Test a list of ordered integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list of unordered integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when the maximum is at the beginning."""
        self.assertEqual(max_integer([9, 2, 3, 1]), 9)

    def test_negative_numbers(self):
        """Test a list with negative numbers."""
        self.assertEqual(max_integer([-5, -9, -1]), -1)

    def test_mixed_numbers(self):
        """Test a list with both positive and negative numbers."""
        self.assertEqual(max_integer([-10, 0, 10, -20]), 10)

    def test_one_element_list(self):
        """Test a list with only one element."""
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        """Test an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test list with float values."""
        self.assertEqual(max_integer([1.5, 3.2, 2.8]), 3.2)

    def test_mixed_int_float(self):
        """Test list with mixed int and float values."""
        self.assertEqual(max_integer([1, 2.5, 3, 2.9]), 3)

    def test_string(self):
        """Test a string (sequence of characters)."""
        self.assertEqual(max_integer("Holberton"), 't')

    def test_list_of_strings(self):
        """Test a list of strings."""
        self.assertEqual(max_integer(["abc", "xyz", "def"]), "xyz")

    def test_none_argument(self):
        """Test passing None as argument."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_iterable(self):
        """Test passing non-iterable argument."""
        with self.assertRaises(TypeError):
            max_integer(5)


if __name__ == "__main__":
    unittest.main()
