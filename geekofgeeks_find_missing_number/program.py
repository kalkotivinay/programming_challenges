# getMissingNo takes list as argument
def getMissingNo(A):
    n = len(A)
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(A)
    return total - sum_of_A

# Driver program to test above function
rinput = raw_input()

ilist = rinput.split(' ')
miss = getMissingNo(list(map(int, ilist)))
print(miss)

