# #!/usr/bin/python3

"""A class that defines a rectangle"""


class Rectangle:
    """Initializes rectangle object
    """
    number_of_instances = 0
    print_symbol = "#"


    def __init__(self, width = 0, height = 0):
        """creates instance of an object
        Args:
            width(int)
            height(int)
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
        

    @property
    def width(self):
        """Retrieves an attribute"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Sets an attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        
    @property
    def height(self):
        """Retrieves an attribute"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Sets an attribute"""
        if not isinstance (value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value
    def area(self):
        """Returns area of a rectangle"""
        return (self.width*self.height)
    def perimeter(self):
        perimeter = 0
        return (2*self.width + 2*self.height)
    def __str__(self):
        """ Prints a rectangle with character #"""
        if self.width == 0 or self.height == 0:
            return ("")
        else:
            rec_str = ""
            for i in range(self.height):
                rec_str += str(Rectangle.print_symbol) * self.width
                if i < self.height - 1:
                    rec_str += "\n"
            return (rec_str)
    def __repr__(self):
        """Prints string representation of a rectangle"""
        return (f"Rectangle({self.width}, {self.height})")
    def __del__(self):
        """Deletes an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1