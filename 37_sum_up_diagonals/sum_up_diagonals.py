def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    diagonal_count = len(matrix[0])
    list_to_sum = []
    x = 0
    while x < diagonal_count:
        for lst in matrix:
            list_to_sum.append(lst[x])
            x+=1
    x-=1
    while x>=0:
        for lst in matrix:
            list_to_sum.append(lst[x])
            x-=1
    return sum(list_to_sum)


