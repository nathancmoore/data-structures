"""Radix Sort."""


def radix_sort(a_list):
    """Use RS to sort the provided list and return it."""
    if not isinstance(a_list, list):
        raise TypeError("Only list is a valid input type!")

    if len(a_list) < 2:
        return a_list

    lst = map(lambda x: str(x), a_list)

    loops = 0

    for num in lst:
        if len(num) > loops:
            loops = int(len(num))

    for idx, num in enumerate(lst):
        if len(num) < loops:
            for i in range(loops - len(num)):
                lst[idx] = '0' + lst[idx]

    for i in range(loops):
        temp = [[] for j in range(10)]
        for num in lst:
            digit = int(num[-1 - i])
            temp[digit].append(num)

        lst = []

        for bucket in temp:
            for x in bucket:
                lst.append(x)

    return map(lambda x: int(x), lst)


if __name__ == '__main__':
    from timeit import timeit
    from random import randint
    good = sorted([randint(1, 1000) for i in range(10)])
    bad = sorted([randint(1, 1000) for i in range(10)], reverse=True)
    ran = [randint(1, 1000) for i in range(10)]

    fast = timeit('radix_sort(good[:])', setup="from __main__ import radix_sort, good")
    slow = timeit('radix_sort(bad[:])', setup="from __main__ import radix_sort, bad")
    medium = timeit('radix_sort(ran[:])', setup="from __main__ import radix_sort, ran")

    print("\nBest case: {}\n".format(fast))
    print("Worst case: {}\n".format(slow))
    print("Random case: {}\n".format(medium))
