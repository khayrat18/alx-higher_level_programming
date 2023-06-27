# #!/usr/bin/python3

class Square:
    def __init__(self,size=0, position=(0,0)):
        """Initializes a square object
        Args: size, value
        Returns: None
        Raises: None 
        """
        self.__size = 0
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves a size square object
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

    @property
    def position(self):
        """Retrieves attribute position square object
        Args: None
        Returns: size retrieved
        Raises: None
        """
        return (self.__position)
    
    @position.setter
    def position(self, value):
        """Sets attribute position a square object
        Args: value
        Returns: None
        Raises: TypeError if size is not an integer if tuple is more thn 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2) or not all(isinstance(1,int) for i in value) or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value 
    def my_print(self):

        if self.__size == 0:
            print ()
        else:
            for i in range (self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range (self.__position[0]):
                    print (" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print ()