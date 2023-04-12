#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = _import_('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def _init_(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (intt): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width".width)
        self._width = width
        self.integer_validator("height".height)
        self._height = height
