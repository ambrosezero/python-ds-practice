def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    return sorted(list(str(num1))) == sorted(list(str(num2)))
    # # first version:
    # # ????? why must list(str(num1)) and num1.sort() be done in seperate steps? in other words,
    # # ????? why doesn't num = list(str(num1)).sort() work?
    # rtnnum1 = list(str(num1))
    # rtnnum2 = list(str(num2))
    # rtnnum1.sort()
    # rtnnum2.sort()
    # if rtnnum1 == rtnnum2:
    #     return True
