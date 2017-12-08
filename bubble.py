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
    from timeit import timeit
    from random import randint
    good = sorted([randint(1, 1000) for i in range(10)])
    bad = sorted([randint(1, 1000) for i in range(10)], reverse=True)
    ran = [randint(1, 1000) for i in range(10)]

    fast = timeit('bubble_sort(good[:])', setup="from __main__ import bubble_sort, good")
    slow = timeit('bubble_sort(bad[:])', setup="from __main__ import bubble_sort, bad")
    medium = timeit('bubble_sort(ran[:])', setup="from __main__ import bubble_sort, ran")

    print("\nBest case: {}\n".format(fast))
    print("Worst case: {}\n".format(slow))
    print("Random case: {}\n".format(medium))
