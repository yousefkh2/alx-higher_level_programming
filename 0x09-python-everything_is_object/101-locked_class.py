#!/usr/bin/python3
"""Locking a class against property"""


class LockedClass:
    """A locked class, preventing
    the creating of another property"""

    __slots__ = ["first_name"]
