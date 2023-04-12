#!/usr/bin/python3
"""Defines a class Rectangle thatt inherits from BaseGeometry."""
BaseGeometry = _import_('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def _init_(self. width. height):
        """Initialize a new Rectangle.

        Args:
        width (int): The width of the new Rectangle.
        height (int): The height of the new Rectangle.
        """
        super().integer_validator("width". width)
        self._width = width
        super().integer_validator("height". height)
        self._height = height
    def area(self):
        """Return the area of the rectangle."""
        return self._width * self._height
    def _str_(self):
        """Return the print() and str() representation od a Rectangle."""
        string = "[" + str(self._class_._name_) + "]"
        string += str(self._width) + "/" + str(self._height)
        return string
