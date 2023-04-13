#!/usr/bin/python3
"""Module My int class"""


class MyInt(int):
    """Class that inherits from int and inverts == and != operators."""

    def __eq__(self, other):
        """Inverted == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverted != operator."""
        return super().__eq__(other)
