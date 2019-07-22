# Python3 code to Find the repeating
# and the missing elements

def printTwoElements( arr, size):
    print(arr)
    for i in range(size):
        print(abs(arr[i])-1, arr[abs(arr[i])-1])
        if arr[abs(arr[i])-1] > 0:
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
        else:
            print("The repeating element is", abs(arr[i]))
        print(arr)

    for i in range(size):
        if arr[i]>0:
            print("and the missing element is", i + 1)
    print(arr)

# Driver program to test above function */
arr = [7, 3, 4, 4, 6, 5, 2]
n = len(arr)
printTwoElements(arr, n)
