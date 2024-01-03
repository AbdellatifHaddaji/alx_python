def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of the specified class;
    otherwise, returns False.
    """
    return type(obj) == a_class
