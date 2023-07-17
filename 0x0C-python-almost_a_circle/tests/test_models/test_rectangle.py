#!/usr/bin/python3
"""Tests for the Rectangle model."""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import sys

def capture_stdout(obj, method):
    """Capture the stdout of a method."""
    capture = io.StringIO()
    sys.stdout = capture
    if method == "print":
        print(obj)
    else:
        obj.display()
    sys.stdout = sys.__stdout__
    return capture

class TestRectangleInstance(unittest.TestCase):
    """Tests for the instantiation of the Rectangle class."""

    def test_for_instance(self):
        """Test if the Rectangle is an instance of Base."""
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_no_arg(self):
        """Test instantiation with no arguments."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Test instantiation with one argument."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_arg_with_no_id(self):
        """Test instantiation with two arguments and no id."""
        b1 = Rectangle(1, 2)
        b2 = Rectangle(2, 1)
        self.assertEqual(b1.id, b2.id - 1)

    def test_y_private(self):
        """Test accessing the private attribute __y."""
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4).__y)

    def test_y_get(self):
        """Test the getter for y."""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter_not_int(self):
        """Test the setter for y with a non-int value."""
        r = Rectangle(5, 7, 7, 5, 1)
        with self.assertRaises(TypeError):
            r.y = "hello"

    def test_y_setter_less(self):
        """Test the setter for y with a negative value."""
        r = Rectangle(5, 7, 7, 5, 1)
        with self.assertRaises(ValueError):
            r.y = -1

    def test_y_setter(self):
        """Test the setter for y."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)

class TestAReaRectangle(unittest.TestCase):
    """Tests for the area of the Rectangle."""

    def test_area_with_pre(self):
        """Test the area method."""
        r = Rectangle(10, 2)
        self.assertEqual(20, r.area())

    def test_area_with_other(self):
        """Test the area method with a Rectangle of different dimensions."""
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(56, r.area())

    def test_area_with_modify(self):
        """Test the area method after modifying the width."""
        r = Rectangle(9, 3)
        r.width = 10
        self.assertEqual(30, r.area())

    def test_area_height(self):
        """Test the area method after modifying the height."""
        r = Rectangle(9, 3)
        r.height = 10
        self.assertEqual(90, r.area())

    def test_area_both(self):
        """Test the area method after modifying both the width and the height."""
        r = Rectangle(1, 2)
        r.width = 11
        r.height = 10
        self.assertEqual(110, r.area())

class TestRectangle_stdout(unittest.TestCase):
    """Tests for the display and print methods of the Rectangle."""

    def test_display_width(self):
        """Test the display method."""
        r = Rectangle(2, 3, 0, 0, 0)
        capture = capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_height(self):
        """Test the display method with a different height."""
        r = Rectangle(4, 3, 0, 0, 0)
        capture = capture_stdout(r, "display")
        self.assertEqual("####\n####\n####\n", capture.getvalue())

    def test_print_a(self):
        """Test the print method."""
        r = Rectangle(1, 2, 3, 4, 5)
        m = "[Rectangle] (5) 3/4 - 1/2"
        self.assertEqual(m, r.__str__())

    def test_print_b(self):
        """Test the print method with a different Rectangle."""
        r = Rectangle(1, 2, id=5)
        m = "[Rectangle] (5) 0/0 - 1/2"
        self.assertEqual(m, str(r))
    
class TestUpdate(unittest.TestCase):
    """test update"""

    def test_update_a(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(5, 4, 3, 2, 1)
        m = "[Rectangle] (5) 2/1 - 4/3"
        self.assertEqual(m, str(r))

    def test_update_b(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        m = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(m, str(r1))

    def test_update_c(self):
        r2 = Rectangle(10, 10, 10, 10)
        r2.update(89, 2)
        m = "[Rectangle] (89) 10/10 - 2/10"
        self.assertEqual(m, str(r2))

    def test_update_with_kwargs(self):
        r3 = Rectangle(10, 10, 10, 10)
        r3.update(id = 89)
        m = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(m, str(r3))

    def test_with_arg_kwargs(self):
        r4 = Rectangle(1, 2, 3, 4, 5)
        r4.update(5, 4, 3, 2, 1, id = 90, width = 48)
        m = "[Rectangle] (5) 2/1 - 4/3"
        self.assertEqual(m, str(r4))

    def test_kwargs_only(self):
        r5 = Rectangle(1, 2, 3, 4, 5)
        r5.update(width = 49, height = 40, x = 2, y = 3, id = 7)
        self.assertEqual(r5.area(), 1960)


class TestToDictionary(unittest.TestCase):
    """Rectangle To Dictionary"""

    def test_to_dict_first(self):
        s1 = Rectangle(2, 4)
        s1.id = 8
        p = {'id': 8, 'width': 2, 'height': 4, 'x': 0, 'y': 0}
        self.assertEqual(s1.to_dictionary(), p)

    def test_to_dict_with_edit(self):
         s1 = Rectangle(2, 4, 5, 6, 7)
         s1.update(6, 5, 4, 5, 6)
         p = {'id': 6, 'width': 5, 'height': 4, 'x': 5, 'y': 6}
         self.assertEqual(s1.to_dictionary(), p)


class TestToJson(unittest.TestCase):
    """Test  for to json"""
    def test_json_first_a(self):
        r1 = Rectangle(10, 7, 2, 8, 9)
        dictionary = r1.to_dictionary()
        p = '[{"x": 2, "width": 10, "id": 9, "height": 7, "y": 8}]'
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), type(p))

    def test_json_first_b(self):
        dictionary = []
        p = '[[]]'
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, p)