'''
You are given two unsorted arrays of distinct integers A and B, where
A has length n and B has length n-1. B is the same array as A, except 
that one element, somewhere in the array, has been deleted. The other 
elements of B are otherwise in exactly the same order as in A. 
Below is an O(log n) algorithm to find the index of that missing
element.
'''

def findMissing(A, a_low, a_high, B, b_low, b_high):
    mid = a_low + (a_high - a_low) // 2

    if a_low == a_high:
        return A[a_low]
    
    if A[mid] == B[mid]:
        return findMissing(A, mid + 1, a_high, B, mid + 1, b_high)

    if A[mid] != B[mid]:
        return findMissing(A, a_low, mid, B, b_low, mid)
    
A = [3,2,1,8,7,5]
B = [3,1,8,7,5]
print(findMissing(A, 0, len(A) - 1, B, 0, len(B) - 1))

A1 = [3,2,1,8,7,5]
B1 = [3,2,1,8,7,]
print(findMissing(A1, 0, len(A1) - 1, B1, 0, len(B1) - 1))