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

    unique_nums = set(nums)
    if len(unique_nums) == len(nums):
        return None
    else:
        counts = {num: nums.count(num) for num in nums}
        for (val, count) in counts.items():
            if count > 1:
                return val 
