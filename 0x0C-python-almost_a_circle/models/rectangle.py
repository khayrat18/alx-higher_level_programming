#!/usr/bin/python3
"""Defines a a Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base
    args:
        width(int)
        height(int)
        x(int)
        y(int)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves an attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets an attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be a integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves an attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets an attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be a integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves an attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets an attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves an attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets an attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Assigns keys and values to arguments"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                if a == 1:
                    self.width = arg
                if a == 2:
                    self.height = arg
                if a == 3:
                    self.x = arg
                if a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns dictionary representaion og attributes"""
        get_dict = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.x
                }
        return get_dict

    def __str__(self):
        """Returns string representation of attributes"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))
