#!/usr/bin/python3
"""Defines a square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle
    Args:
        size(int)
        x(int)
        y(int)
        id(int)
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves value of attributs"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets value of attribute"""
        self.width = value
        self.height = value

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
        """Returns dictionary representtaion of attributes"""
        get_dict = {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
        return get_dict

    def __str__(self):
        """Returns string representation of attributes"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))
