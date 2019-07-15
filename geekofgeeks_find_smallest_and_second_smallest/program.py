# Python program to find smallest and second smallest elements
import sys

def print2Smallest(arr):
    # There should be atleast two elements
    arr_size = len(arr)
    if arr_size < 2:
        print "Invalid Input"
        return

    first = second = sys.maxint
    for i in arr:
        # If current element is smaller than first then
        # update both first and second
        if i < first:
            second = first
            first = i
        # If arr[i] is in between first and second then
        # update second
        elif (i < second and i != first):
            second = i

    if (second == sys.maxint):
        print "No second smallest element"
    else:
        print('The smallest element is %d and second smallest element is %d' % (first, second))

# Driver function to test above function
arr = [12, 13, 1, 20, 34, 1]
print2Smallest(arr)