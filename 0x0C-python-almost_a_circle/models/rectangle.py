#!/usr/bin/python3

"""Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """
    A class used to represent an Rectangle

    Attributes
    ----------
    width : int
        width of the rectangle
    height : int
        height of the rectangle
    x : int
        x axis of the rectangle
    y : int
        y axis of the rectangle

    methods
    ------
    area()
        returns area of rectangle
    display(self)
        displays the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        width : int
            The width of the rectangle
        height : int
            The height of the rectangle
        x : int
            The x axis
        y : int
            The y axis
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """ returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Parameters
        ----------
        value : int
            sets the width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Parameters
        ----------
        value : int
            sets the height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns the x axis of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Parameters
        ----------
        value : int
            sets the x axis of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns y axis of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Parameters
        ----------
        value : int
            sets y axis of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """
        displays the rectangle
        """
        x = self.__x
        h = self.__height
        w = self.__width
        print("\n" * self.__y, end="")
        pattern = [" " * x + "#" * w for i in range(h)]
        print("\n".join(pattern))

    def __str__(self):
        """
        displays info the rectangle
        """
        i = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return f"[Rectangle] ({i}) {x}/{y} - {w}/{h}"

    def update(self, *args, **kwargs):
        """
        Parameter
        --------
        args : varying number of arguments
            used to update the attributes of the rectangle
        kwargs : varying number of key word arguments
            used to update the attributes of the rectangle
        """
        if len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        returns the dictionary representation of Rectangle
        """
        return {
            "x": getattr(self, "x"),
            "y": getattr(self, "y"),
            "id": getattr(self, "id"),
            "height": getattr(self, "height"),
            "width": getattr(self, "width")
            }
