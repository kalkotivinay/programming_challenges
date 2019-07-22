# Python3 code to Find the repeating
# and the missing elements

def printTwoElements( arr, size):
    d = {}
    i = 0
    while (i < len(arr)):
        d[i] = 0
        i += 1

    for a in arr:
        d[a - 1] += 1

    for k,v in d.items():
        if v == 0:
            print("Missing number %d" % (k+1))
        if v == 2:
            print("Duplicate number %d" % (k+1))
    print(d)


# Driver program to test above function */
arr = [7, 3, 4, 6, 5, 6, 1]
n = len(arr)
print(arr)
printTwoElements(arr, n)