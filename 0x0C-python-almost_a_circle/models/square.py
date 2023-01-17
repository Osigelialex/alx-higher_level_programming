#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class used to represent a Square

    Attributes
    ----------
    size : int
        The size of the square
    x : int
        The x axis of the square
    y : int
        The y axis of the square
    id : int or None
        The id of the Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor of square class

        Parameters
        ---------
         size : int
            The size of the square
         x : int
            The x axis of the square
         y : int
            The y axis of the square
         id : int or None
            The id of the Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns the string representation of square object
        """
        i = self.id
        x = self.x
        y = self.y
        s = self.width
        return f"[Square] ({i}) {x}/{y} - {s}"

    @property
    def size(self):
        """
        getter function for width and height(size)
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter function for width and height(size)
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates attributes of square

        Parameters
        ----------
        args : variable number of arguments
        kwargs : variable number of key word arguments
        """
        if len(args) != 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        returns the dictionary representation of the Square class
        """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.width,
            "y": self.y
            }
