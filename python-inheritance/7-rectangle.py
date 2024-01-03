class BaseGeometry:
    """BaseGeometry class with area and integer_validator methods."""
    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value:
        - If value is not an integer: raise a TypeError exception with the message '<name> must be an integer'
        - If value is less or equal to 0: raise a ValueError exception with the message '<name> must be greater than 0'
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""
    def __init__(self, width, height):
        """Instantiation with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the rectangle description in the format [Rectangle] <width>/<height>."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

# Example usage
if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
