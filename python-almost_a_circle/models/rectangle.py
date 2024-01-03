
""" Rectangle Module """
from models.base import Base

class Rectangle(Base):
    """ Rectangle class inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes a new instance of Rectangle """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
