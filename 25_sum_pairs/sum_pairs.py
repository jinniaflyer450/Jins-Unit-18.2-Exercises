def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    current_index1 = 0
    current_index2= 1
    matched_pairs = {}
    for num in nums:
        to_search = nums[current_index2::]
        for val in to_search:
            if num + val == goal:
                matched_pairs[(num, val)] = (current_index1, current_index2)
            current_index2+=1
        current_index1+=1
        current_index2 = current_index1+1
    compare_items = [[None, None], len(nums), len(nums)]
    for item in matched_pairs.items():
        first_num = item[0][0]
        second_num = item[0][1]
        first_index = item[1][0]
        second_index = item[1][1]
        if second_index < compare_items[2]:
            compare_items[0][0] = first_num
            compare_items[0][1] = second_num
            compare_items[1] = first_index
            compare_items[2] = second_index
    if compare_items[0] == [None, None]:
        return ()
    else:
        return (compare_items[0][0], compare_items[0][1])


