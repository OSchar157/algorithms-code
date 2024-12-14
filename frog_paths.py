'''
There are n rocks in a river arranged in a line, and a frog is using
them to jump across. At each step, the frog can either jump one rock
ahead or two rocks ahead. Also the frog must land on the first rock and
the last rock. What are the number of the feasible paths that the frog can take?
Below is a O(n) dynamic programming solution to the problem
'''

def numJumps(n):
    # base case
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    # method of storage for our solution
    jumps = [0]*(n + 1)

    # base case (jumps[0] = 0 already defined)
    jumps[1] = 1
    jumps[2] = 1

    # recursive relation
    for i in range(3, n + 1):
        jumps[i] = jumps[i - 1] + jumps[i - 2]

    # return the answer
    return jumps[n]

print(numJumps(9))