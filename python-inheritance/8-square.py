class BaseGeometry:
    """Base class with an integer validator method"""

    def area(self):
        """Raise an exception indicating that area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer and greater than 0"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return a string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Compute the area of the rectangle"""
        return self.__width * self.__height

class Square(Rectangle):
    """Square class inheriting from Rectangle"""

    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)

    def __str__(self):
        """Return a string representation of the square"""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
