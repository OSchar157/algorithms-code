'''
This is a solution to the Bachet's game problem
https://open.kattis.com/contests/mar3q8/problems/bachetsgame
'''
def bachets(num_stones, removal_opts):
    # define our method of storage for our solution
    sol = [False] * (num_stones + 1)

    # no base cases needed

    # recursive relationship
    for i in range(1, num_stones + 1):
        for opt in removal_opts:
            if i - opt >= 0 and sol[i - opt] == False:
                sol[i] = True
                break

    return "Stan wins" if sol[num_stones] else "Ollie wins"


from sys import stdin

for line in stdin:
    line = line.strip().split()
    num_stones = int(line[0])
    removalOpts = list(map(int, line[2:]))
    print(bachets(num_stones, removal_opts))
