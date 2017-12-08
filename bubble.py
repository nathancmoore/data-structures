"""Bubble sort."""


def bubble_sort(a_list):
    """Use BS to sort the provided list and return it."""
    if not isinstance(a_list, list):
        raise TypeError("Only list is a valid input type!")

    if len(a_list) < 2:
        return a_list

    loops = 0
    while True:
        swaps = 0
        for i in range(len(a_list) - 1 - loops):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                swaps += 1
        if swaps == 0 or len(a_list) - loops == 2:
            return a_list
        loops += 1

if __name__ == '__main__':
    a = [9, 7, 10, 35, 2, 6, 1, 300, 26, 99]
    b = []
    c = [6]
    d = [1, 2, 3, 4, 5, 6]
    e = [3, 3, 3]

    print(bubble_sort(a))
    print(bubble_sort(b))
    print(bubble_sort(c))
    print(bubble_sort(d))
    print(bubble_sort(e))
