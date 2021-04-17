def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_string = f'{num1}'
    num2_string = f'{num2}'
    num1_freq = {digit: num1_string.count(digit) for digit in num1_string}
    num2_freq = {digit: num2_string.count(digit) for digit in num2_string}
    if num1_freq == num2_freq:
        return True
    else:
        return False