'''
There are a series of balloons floating towards you along a road.
Your input array Balloons gives a schedule of the total number of
balloons that will be at your position at time i.

You are a monkey trying to pop these balloons with darts. 
If you throw a dart at time i, it will pop any balloons in front of you at
time i, as well as some of the balloons behind. Your darts have
piercing factor p, which means that throwing a dart at time i will
pop all the balloons in the array at times i, i + 1, ..., i + p-1.

If you had unlimited darts, you could pop all the balloons. However, you only
have a limited k darts, so you must choose wisely about when to throw the
darts. Your goal is to pop as many balloons as possible.

Below is an O(nk) solution that utalizes dynamic programming
'''
def maxPops(Balloons, k, p):
    n = len(Balloons)

    # define method of storage for our solution
    sol = [[0] * (k + 1) for _ in range(n + 1)]
    # will hold the running sum of ballons
    running_sum = [0] * (n + 1)

    # need to calculate the first index for out or range errors
    running_sum[0] = sum(Balloons[:p])

    # Calculate runningSum[i]
    for i in range(1, n - p):
        running_sum[i] = running_sum[i - 1] + Balloons[i + p - 1] - Balloons[i - 1]

    # base cases
    # sol[0][d] = 0 for all d
    # sol[i][0] = 0 for all i

    # recursive relation
    for i in range(1, n + 1):
        for d in range(1, k + 1):
            sol[i][d] = max(sol[i - 1][d], sol[i - p][d - 1] + running_sum[i - p])

    return sol[n][k]