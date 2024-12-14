'''
Given 64 bit inputs a,k,n, the goal is to compute a^k % n.
This solution takes note of the fact that for any integers x,y, xy % n = (x % n)(y % n) % n.
The solution below runs in O(log k).
'''
def expAndMod(a, k, n):
    # Base cases
    if k == 0:
        return 1
    if k == 1:
        return a

    # If k is even, we can simply divide and multiply the result by itsself
    # we save the result in a variable so we don't call the same function twice
    # we use the general form xy%n = (x%n * y%n) % n to significanly save on space
    if k % 2 == 0:
        r = expAndMod(a, k / 2, n)
        return ((r % n) * (r % n)) % n
    # If k is odd, we need to multiply the result of k - 1 by a 
    # a^{k - 1} == a * a^k
    else:
        r = expAndMod(a, (k - 1) / 2, n)
        return ((a % n) * (((r % n) * (r % n)) % n )) % n

print(expAndMod(1234567890,1234567890,987654321) == 385198425)
