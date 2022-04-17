def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """

    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.
    return (sorted(set(ages))[-2], sorted(set(ages))[-1])

    # ?????     in problems such as this one and the one before (#34), my answer is a one line combination of
    # ?????     methods and functions that fill the requirements, but in many cases the solution is more
    # ?????     lengthy and slightly more complex. is there a downside to the way i am doing it? is it against
    # ?????     "best practices" conventions, or is there some other reason it is undesirable aside from
    # ?????     complexity in reading?
