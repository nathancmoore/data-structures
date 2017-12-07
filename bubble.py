"""Bubble sort."""


def bubble_sort(list):
    """Use BS to sort the provided list and return it."""
    output_list = []
    while list:
        if len(list) > 1:
            for i in range(len(list) - 1):
                if list[i] > list[i + 1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
        output_list.append(list.pop(-1))

    return output_list[::-1]

if __name__ == '__main__':
    a = [9, 7, 10, 35, 2, 6, 1, 300, 26, 99]

    print(bubble_sort(a))
