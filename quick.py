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


if __name__ == '__main__':
    from timeit import timeit
    from random import randint
    good = sorted([randint(1, 1000) for i in range(10)])
    bad = sorted([randint(1, 1000) for i in range(10)], reverse=True)
    ran = [randint(1, 1000) for i in range(10)]

    fast = timeit('quick_sort(good[:])', setup="from __main__ import quick_sort, good")
    slow = timeit('quick_sort(bad[:])', setup="from __main__ import quick_sort, bad")
    medium = timeit('quick_sort(ran[:])', setup="from __main__ import quick_sort, ran")

    print("\nPre-Sorted: {}\n".format(fast))
    print("Pre-Sorted and Reversed: {}\n".format(slow))
    print("Random: {}\n".format(medium))
