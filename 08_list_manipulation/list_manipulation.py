def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """

    if location not in ['end', 'beginning'] or command not in ['add', 'remove']:
        return None
    if command == "remove":
        #  ?????? why must i use a different index number for 'add' vs 'remove'? here I have len(lst)-1 ....
        settings = {'end': len(lst)-1, 'beginning': 0}
        return lst.pop(settings[location])
    elif command == "add":
        #  ?????  ..... but here i have just len(lst)
        settings = {'end': len(lst), 'beginning': 0}
        lst.insert(settings[location], value)
        return lst
    else:
        return None


# print('dog')
