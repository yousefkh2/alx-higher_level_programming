#!/usr/bin/python3
"""Defining the base class."""
import json


class Base:
    """Base class for this model."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance.

        Args:
            id : Identifier for each instance.
        """
        self.id = id if id is not None else self.__increase_counter()

    def __increase_counter(self):
        """Increase the counter and returns the current value."""
        Base.__nb_objects += 1
        return (Base.__nb_objects)

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to JSON string."""
        return (json.dumps(list_dictionaries) if list_dictionaries else "[]")

    @classmethod
    def save_to_file(cls, list_objs):
        """Save the instance of the object to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as myfile:
            list_dicts = [obj.to_dictionary() for obj in list_objs] if list_objs else []
            myfile.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Convert JSON string to a list."""
        return (json.loads(json_string) if json_string else [])

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set from a dictionary."""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return (new)

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as myfile:
                list_dicts = cls.from_json_string(myfile.read())
                return ([cls.create(**dictionary) for dictionary in list_dicts])
        except IOError:
            return ([])
            