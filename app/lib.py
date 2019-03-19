def normalize(data, n):
    """
    >>> normalize([2, 15, 28, 100, 2, 0, 15, 1], 2)
    [2, 15, 2, 15]
    """

    min_list = data[:]
    min_list.sort()
    min_list = min_list[:n]

    max_list = data[:]
    max_list.sort(reverse=True)
    max_list = max_list[:n]

    result = []
    for number in data:
        if number not in min_list and number not in max_list:
            result.append(number)

    return result
