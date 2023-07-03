# #!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """Initializes rectangle object
    """


    def __init__(self, width = 0, height = 0):
        """creates instance of an object
        Args:
            width(int)
            height(int)
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves an attribute"""
        return self.__width
    @width.setter
    def width(self, value):
        """Sets an attribute"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        
    @property
    def height(self):
        """Retrieves an atribute"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """ Set an attribute"""
        self.__height = value
        if not isinstance (value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        
