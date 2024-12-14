'''
Given two sequences X and Y, let C(X,Y) denote the number of times
that X appears as subsequence of Y (all the letters of X, in order).
For instance, the sequence ABC appears 27 times as a subsequence of
AAABBBCCC.
Below is an O(mn) solution that utalizes dynamic programming.
'''
def C(X, Y):
    # define our method of storage for the solution
    sol = [[0] * (len(Y) + 1) for _ in range(len(X) + 1)]

    # base case (if X is "", then its a solution to all Y[i])
    for j in range(len(Y) + 1):
        sol[0][j] = 1
    
    # recursive relation
    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            if X[i - 1] == Y[j - 1]:
                sol[i][j] = sol[i][j - 1] + sol[i - 1][j - 1]
            else:
                sol[i][j] = sol[i][j - 1]
    
    return sol[len(X)][len(Y)]