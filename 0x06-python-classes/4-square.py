# #!/usr/bin/python3

class Square:
    """ A class that defines a square object
    """
    def __init__(self,size=0):
        """Initializes a square object
        Args: size
        Returns: None
        Raises: None
        """
        self.__size = 0
        self.size = size

    @property
    def size(self):
        """Retrieves size square object
        Args: None
        Returns: size retrieved
        Raises: None
        """
        return (self.__size)
        
    @size.setter
    def size(self, value):
        """Sets size a square object
        Args: value
        Returns: None
        Raises: TypeError if size is not an integer, ValueError if size is less than 0
        """
        if not isinstance(value,int):
            raise TypeError("size must be integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns current square area
        Args: None
        Returns: current square area
        Raises: None 
        """
        return (self.size ** 2)
    