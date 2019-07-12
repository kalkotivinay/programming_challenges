Find missing number

You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list. One of the integers is missing in the list.

Write an efficient code to find the missing integer.

Example :

Input: arr[] = {1, 2, 4,, 6, 3, 7, 8}
Output: 5

Input: arr[] = {1, 2, 3, 5}
Output: 4


METHOD 1(Use sum formula)
Algorithm:

1. Get the sum of numbers which is total = n*(n+1)/2
2. Subtract all the numbers from sum and
   you will get the missing numbers

