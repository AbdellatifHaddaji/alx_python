
""" Square Module """
from models.rectangle import Rectangle

class Square(Rectangle):
    """ Square class inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a new instance of Square """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value
