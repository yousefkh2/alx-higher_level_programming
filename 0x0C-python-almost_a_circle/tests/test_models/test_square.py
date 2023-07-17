#!/usr/bin/python3
"""The test module for square.py"""
from models.rectangle import Rectangle
from models.square import Square
import unittest
import io
import sys


class TestSquareInstatiation(unittest.TestCase):
    """Class for testing Square instantiation"""

    def test_instance_a(self):
        """Tests if the id attribute is incrementing"""
        s1 = Square(1, 2, 3)
        s2 = Square(4, 3, 2)
        self.assertEqual(s1.id, s2.id - 1)

    def test_instance_with_id(self):
        """Tests if the id attribute is set correctly"""
        s1 = Square(2, 3, 4, 5)
        self.assertEqual(s1.id, 5)

    def test_instance_b(self):
        """Tests if exception is raised when no argument is provided"""
        with self.assertRaises(TypeError):
            Square()

    def test_instance_id(self):
        """Tests if id can accept non-integer values"""
        s1 = Square(2, 3, 4, 'boy')
        self.assertEqual(s1.id, 'boy')

    def test_instance_from(self):
        """Tests if square is an instance of Rectangle"""
        s1 = Square(3)
        self.assertIsInstance(s1, Rectangle)


class TestChangecase(unittest.TestCase):
    """Class for testing attribute changes in Square class"""

    def test_update_x(self):
        """Tests if x attribute is updated properly"""
        s1 = Square(1, 2, 4, 5)
        s1.x = 9
        self.assertEqual(s1.x, 9)

    def test_get_width_height(self):
        """Tests if width and height attributes are equal"""
        s1 = Square(2)
        self.assertEqual(s1.width, s1.height)


class TestPrintSquare(unittest.TestCase):
    """Class for testing str representation of Square class"""

    def test_width_height_only(self):
        """Tests the str representation when only width and height are defined"""
        s1 = Square(2)
        s1.id = 4
        m = "[Square] (4) 0/0 - 2"
        self.assertEqual(m, str(s1))

    def test_all_define(self):
        """Tests the str representation when all attributes are defined"""
        s1 = Square(4, 3, 2, 5)
        d = "[Square] (5) 3/2 - 4"
        self.assertEqual(d, s1.__str__())

    def test_x_or_y_change(self):
        """Tests the str representation when x or y attributes are changed"""
        s1 = Square(4, 3, 2, 5)
        s1.x = 25
        d ="[Square] (5) 25/2 - 4"
        self.assertEqual(d, s1.__str__())


class TestSizeSetterGetter(unittest.TestCase):
    """Class for testing getter and setter of size attribute"""

    def test_compare_height(self):
        """Tests if size and height attributes are equal"""
        s1 = Square(4)
        self.assertEqual(s1.size, s1.height)

    def test_compare_width(self):
        """Tests if size and width attributes are equal"""
        s1 = Square(4)
        self.assertEqual(s1.size, s1.width)

    def test_update_size_a(self):
        """Tests if size attribute updates both height and width attributes"""
        s1 = Square(5)
        s1.size = 8
        self.assertEqual(s1.height, 8)
        self.assertEqual(s1.width, 8)
        self.assertEqual(s1.height, s1.width)
        self.assertEqual(s1.width, s1.size)

    def test_first_error(self):
        """Tests if non-integer size value raises TypeError"""
        s2 = Square(7)
        with self.assertRaises(TypeError):
            s2.size ='boy'

    def test_second_error(self):
        """Tests if negative size value raises ValueError"""
        s2 = Square(8)
        with self.assertRaises(ValueError):
            s2.size = -4


class TestSquare_stdout(unittest.TestCase):
    """Class for testing standard output and update of Square class"""

    @staticmethod
    def capture_stdout(rect, value):
        """Helper function to capture the stdout"""
        capture = io.StringIO()
        sys.stdout = capture
        if value == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return (capture)

    def test_display_a(self):
        """Tests the display method output"""
        s1 = Square(3)
        value = TestSquare_stdout.capture_stdout(s1, 'display')
        self.assertEqual('###\n###\n###\n', value.getvalue())

    def test_display_b(self):
        """Tests the display method output when size attribute changes"""
        s1 = Square(3)
        s1.size = 2
        value = TestSquare_stdout.capture_stdout(s1, 'display')
        self.assertEqual('##\n##\n', value.getvalue())

    def test_args_first(self):
        """Tests the update method with positional arguments"""
        s1 = Square(4, 3, 2, 1)
        s1 = Square(4, 3, 2, 1)
        s1.update(4, 2, 3, 7)
        self.assertEqual(s1.area(), 4)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 7)
        self.assertEqual(s1.id, 4)

    def test_incomplete_args(self):
        s1 = Square(7)
        s1.update(3)
        self.assertEqual(s1.area(), 49)
        self.assertEqual(s1.x, s1.y)
        self.assertEqual(s1.id, 3)

    def test_arg_with_kwargs(self):
        s1 = Square(4)
        s1.update(7, 8, 9, 6, id = 20, size = 4, x = 2, y = 4)
        self.assertEqual(s1.area(), 64)
        self.assertEqual(s1.x, s1.y + 3)
        self.assertEqual(s1.id, 7)

    def test_kwargs_only(self):
        s1 = Square(7)
        s1.update(id = 20, size = 4, x = 2, y = 4)
        self.assertEqual(s1.area(), 16)
        self.assertEqual(s1.x, s1.y / 2)
        self.assertEqual(s1.id, 20)


class TestSquareToDict(unittest.TestCase):
    """convert square to dict representation"""

    def test_dict_first(self):
        s1 = Square(2, 3, 4, 5)
        m = {'id': 5, 'x': 3, 'size': 2, 'y': 4}
        self.assertEqual(s1.to_dictionary(), m)

    def test_dict_second(self):
        s1 = Square(2)
        s1.update(3, 4, 5, 6)
        m = {'id': 3, 'x': 5, 'size': 4, 'y': 6}
        self.assertEqual(s1.to_dictionary(), m)