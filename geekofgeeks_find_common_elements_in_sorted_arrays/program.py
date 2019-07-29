


def findCommon(arr1, arr2, arr3, n1, n2, n3):
    len1 = len(arr1)
    len2 = len(arr2)
    len3 = len(arr3)

    i1 = i2 = i3 = 0

    while (i1 < n1 and i2 < n2 and i3 < n3):
        if (arr1[i1] == arr2[i2]) and (arr2[i2] == arr3[i3]):
            print(arr1[i1])
            i1 += 1
            i2 += 1
            i3 += 1
        elif arr1[i1] < arr2[i2]:
            i1 += 1
        elif arr2[i2] < arr3[i3]:
            i2 += 1
        else:
            i3 += 1
    return



# Driver program to check above function
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
n1 = len(ar1)
n2 = len(ar2)
n3 = len(ar3)
print "Common elements are: \n"
findCommon(ar1, ar2, ar3, n1, n2, n3)