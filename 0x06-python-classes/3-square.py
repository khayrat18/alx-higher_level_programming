# #!/usr/bin/python3

class Square:
    """ A class that represents a sqaure object
    """
    def __init__(self, size=0):
        """Initializes a square object
        Args: size
        Returns: current square area
        Raises: TypeError if size is not an integer, ValueError if size is less than 0
        """
        self._size = size
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
     """Returns current square area of a square object
        Args: None
        Returns: current square area
        Raises: None 
        """
     return (self._size**2)
    
    
