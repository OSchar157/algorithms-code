'''
You are a lazy and somewhat messy student, trying to manage their
messy room over the n days in the semester. Your room
starts out with messiness[0] = 0 before day 0.

On day i, your room will increase in messiness by mess[i] (known in
advance). This mess accumulates over time, and makes you unhappy.
The mental health cost from having a messy room is equal to the total
messiness on day i.

On each day, you can also clean your room, which will reduce the messiness
to 0, but cleaning your room will give you a fixed mental health cost of
cleanCost.

There are n total days in the semester, and you must clean your room
before you move out on day n (even if there's no mess!).

Your goal is to minimize the total mental health cost from messiness/cleaning over the semester.

Below is an O(n^2) solution that utalizes dynamic programming.
'''
def dirtyroom(mess, cleanCost):
    n = len(mess)

    # define our method of storage for our solution
    sol = [float('inf')] * n

    # pre calculate cummulated costs
    cummulated_cost = [0] * (n + 1)
    for i in range(1, n):
        cummulated_cost[i] = cummulated_cost[i - 1] + mess[i - 1]

    # pre compute mental health costs from day when we check solution to current day
    mh_cost = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            mh_cost[i][j] = mh_cost[i][j-1] + (cummulated_cost[j] - cummulated_cost[i+1])
    
    # pre compute the mental health costs if we didnt clean up to current day
    didnt_clean = [0] * n
    for i in range(n):
        didnt_clean[i] = didnt_clean[i - 1] + cummulated_cost[i]

    # base case
    sol[0] = cleanCost

    # recursive relation
    for i in range(1, n):
        # check if we didnt clean except for the last day
        best = didnt_clean[i]
    
        # try every other day
        for j in range(i):
            cost = sol[j] + mh_cost[j][i] 
            best = min(best, cost)
        
        sol[i] = cleanCost + best

    return sol[n-1]

#test 1
mess = [2, 5, 3, 4, 3, 2, 6, 3, 3]
cleanCost = 10
expectedOutput = 56, [1,3,6,8]
print(dirtyroom(mess,cleanCost) == expectedOutput[0])

#test 2
mess = [3,0]
cleanCost = 10
expectedOutput = 13, [1]
print(dirtyroom(mess,cleanCost) == expectedOutput[0])

#test 3
mess = [3,0,0,0,0,0]
cleanCost = 10
expectedOutput = 20, [0,5]
print(dirtyroom(mess,cleanCost) == expectedOutput[0])