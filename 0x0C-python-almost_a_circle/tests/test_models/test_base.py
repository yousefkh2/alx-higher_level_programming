#!/usr/bin/python3
"""Tests for model/base.py"""
import unittest
from models.base import Base


class TestBaseInstatiation(unittest.TestCase):
    """Testing instantiation of the Base class."""

    def setUp(self):
        """Reset the class-wide private variable before each test."""
        Base._Base__nb_objects = 0

    def test_no_args(self):
        """Test instantiation with no arguments."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_with_id(self):
        """Test instantiation with a specific id."""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_three_with_a_unique(self):
        """Test instantiation with and without specific ids."""
        b1 = Base()
        b2 = Base(13)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)
        self.assertNotEqual(b3.id, b2.id + 1)

    def test_string_instance(self):
        """Test instantiation with a string."""
        self.assertEqual("Hello", Base("Hello").id)

    def test_get_instance(self):
        """Test if nb_objects can be accessed directly."""
        with self.assertRaises(AttributeError):
            print(Base().__nb_objects)

    def test_none_instance(self):
        """Test instantiation with None."""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_for_float(self):
        """Test instantiation with a float."""
        self.assertEqual(5.5, Base(5.5).id)

    def test_for_list(self):
        """Test instantiation with a list."""
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_for_dict(self):
        """Test instantiation with a dictionary."""
        self.assertEqual({'a': 2, 'b': 3}, Base({'a': 2, 'b': 3}).id)

    def test_for_complex(self):
        """Test instantiation with a complex number."""
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_for_range(self):
        """Test instantiation with a range."""
        self.assertEqual(range(5), Base(range(5)).id)

    def test_two_args(self):
        """Test instantiation with more than one argument."""
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == "__main__":
    unittest.main()
import unittest

class TestBaseClass(unittest.TestCase):
    """Tests for the Base class."""

    def setUp(self):
        """Reset the class-wide private variable before each test."""
        Base._Base__nb_objects = 0
    
    def test_id_assignment(self):
        """Test for id assignment."""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
    
    def test_id_assignment_specific(self):
        """Test for id assignment with a specific id."""
        base3 = Base(98)
        self.assertEqual(base3.id, 98)

    def test_to_json_string(self):
        """Test for to_json_string"""
        test_dict = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        json_dict = Base.to_json_string([test_dict])
        self.assertTrue(isinstance(json_dict, str))
