"""Quick sort."""


def quick_sort(a_list):
    """Quick sort a list."""
    if not isinstance(a_list, list):
        raise TypeError("Only list is a valid input type!")
    if len(a_list) < 2:
        return a_list
    if len(a_list) == 2 and a_list[0] <= a_list[1]:
        return a_list

    ref = [a_list.pop(0)]
    smaller = []
    bigger = []

    for x in a_list:
        if x < ref[0]:
            smaller.append(x)

        else:
            bigger.append(x)

    return quick_sort(smaller) + ref + quick_sort(bigger)
