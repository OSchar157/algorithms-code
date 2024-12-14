from bisect import bisect_left

'''
Find the length of the longest increasing subsequence in 
an array A of length n.
Below is an O(log n) solution to the problem.
'''
def LIS(A):
    # define our method of storage for the solution
    best = [float('inf')]*len(A)

    # no base cases needed

    # recursive relation
    for i in range(len(A)):
        search = bisect_left(best, A[i]) # bisect_left returns where element should go if its not found
        best[search] = A[i]
    
    # keep counting the number of elements in best excluding infs, this is the LIS
    return sum(x < float('inf') for x in best)


A = [1,2,4,6,3,7,5]
print(LIS(A))
