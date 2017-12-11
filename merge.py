"""Merge sort."""


def merge_sort(a_list):
    """Use MS to sort the provided list and return it."""
    if not isinstance(a_list, list):
        raise TypeError("Only list is a valid input type!")

    if len(a_list) < 2:
        return a_list

    parts = []

    output = []

    for x in a_list:
        parts.append([x])

    while len(parts) > 1:
        if len(parts[0]) == len(parts[1]):
            parts.insert(0, _merge(parts.pop(0), parts.pop(1)))
        else:
            parts.insert(0, _merge(parts.pop(0), _merge(parts.pop(1), parts.pop(2)))


def _merge(part_a, part_b):
    """."""
    temp = []
    while part_a and part_b:
        if part_a[0] <= part_b[0]:
            temp.append(part_a.pop(0))
        else:
            temp.append(part_b.pop(0))

    while part_a:
        temp.append(part_a.pop(0))

    while part_b:
        temp.append(part_b.pop(0))

    return temp
