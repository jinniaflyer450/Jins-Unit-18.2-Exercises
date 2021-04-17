def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    greater_count = 0
    current_index = 0
    for num in nums:
        if current_index < len(nums):
            check_numbers=nums[current_index+1::]
            for val in check_numbers:
                if val > num:
                    greater_count+=1
                else:
                    continue
            current_index+=1
        else:
            break
    return greater_count

