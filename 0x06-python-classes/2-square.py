# #!/usr/bin/python3

class Square:
    """ A class that represents a square object
    """
    def __init__(self,size=0):
        """Initializes a square object
        Args: size
        Returns: None
        Raise: TypeError if size is not an integer, ValueError if size is less than 0
        """
        self.__size = size
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        