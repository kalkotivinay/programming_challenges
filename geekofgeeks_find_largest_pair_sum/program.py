


def findLargestSumPair(array):
    alen = len(array)

    first = second = None
    if array[0] > array[1]:
        second = first
        first = array[0]
    else:
        first = array[1]
        second = array[0]

    for a in array[2:]:
        if a > first:
            second = first
            first = a
        elif a > second and a != first:
            second = a
    return (first + second)


arr = [12, 34, 10, 6, 40]

print(findLargestSumPair(arr))

