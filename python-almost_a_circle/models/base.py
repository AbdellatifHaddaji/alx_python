#!/usr/bin/python3
""" Base Module """

class Base:
    """ Base class for all other classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes a new instance of Base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
