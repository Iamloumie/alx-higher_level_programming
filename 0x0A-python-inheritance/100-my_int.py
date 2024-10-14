#!/usr/bin/python3
"""writing a class"""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, other):
        """Override the == operator with != behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the != operator with behaviour."""
        return super().__eq__(other)
