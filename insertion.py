"""Insertion sort."""


def insertion_sort(a_list):
    """Use IS to sort the provided list and return it."""
    if not isinstance(a_list, list):
        raise TypeError("Only list is a valid input type!")

    if len(a_list) < 2:
        return a_list

    for i in range(len(a_list) - 1):
        print("sorting {}".format(a_list[i + 1]))
        current = a_list[i + 1]
        a_list[i + 1] = None
        idx = i
        while idx >= 0:
            if a_list[idx] < current:
                a_list[idx + 1] = current
                break
            else:
                if idx == 0:
                    a_list[0], a_list[1] = current, a_list[0]
                    break
                else:
                    a_list[idx], a_list[idx + 1] = a_list[idx + 1], a_list[idx]
                    idx -= 1

    return a_list
