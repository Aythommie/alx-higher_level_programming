#!/usr/bin/python3
"""Defines an inherited list class Mylist."""

class Mylist(listt):
    """Implements sorted printing for the builtt-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
