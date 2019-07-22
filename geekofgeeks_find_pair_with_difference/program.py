


def findPair(arr, n):
    for i in arr:
        if n + i in arr:
            print(i, n+i)
            return
    print("No pair for %d" % n)
    return

arr = [90, 70, 20, 80, 50]
n = 45
print(arr)
print(n)
findPair(arr, n)