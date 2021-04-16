def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """

    even_nums = [num for num of nums if num%2 == 0]
    if len(even_nums) == 0:
        return 1
    else:
        for num of even_nums:
            product = product * num
        return product