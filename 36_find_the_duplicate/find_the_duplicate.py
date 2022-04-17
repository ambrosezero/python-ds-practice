def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    # if sorted(nums) == sorted(set(nums)):
    #     return None

    for i in list(range(0, len(nums)-1)):
        if sorted(nums)[i] == sorted(nums)[i+1]:
            return sorted(nums)[i]
    return None

    #     return None
    # return [nums[i] for i in list(range(0, len(nums)-1)) if sorted(nums)[i] != sorted(set(nums))[i]]
