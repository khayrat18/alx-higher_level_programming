# #!/usr/bin/python3

class Square:
    def __init__(self,size=0):
        """Initialiazes a square object
        Args: Size
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
        """Sets attribute a square object
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
    
    def my_print(self):
        """Prints charcater # to stdout
        Args: None
        Returns: None
        Raises: None 
        """
        if self.__size == 0:
            print ()
        else:
            for i in range (self.__size):
                for j in range(self.__size):
                    print ("#", end="")
                print ()