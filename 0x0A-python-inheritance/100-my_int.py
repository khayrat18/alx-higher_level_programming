#!/usr/bin/python3

#!/usr/bin/python3
"""
Module for MyInt class that inherits from int
"""

class MyInt(int):
    """MyInt class that inherits from int
    """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)