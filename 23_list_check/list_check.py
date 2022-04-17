def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    # return all([True for item in lst if isinstance(item, list)])
    return all(True if isinstance(item, list) else False for item in lst)
