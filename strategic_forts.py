'''
You're given an array of n numbers, representing elevation levels of n
forts spaced one mile apart on a mountain range in an East/West direction. 
A fort is called "strategic" if it has a higher or equal elevation than the
other forts within k miles - the (up to) k forts to the East and the (up
to) k forts to the west.
Below is a O(k logk) solution.
'''

def findStrategicFort(forts, low, high, k):
    if high == low:
        return forts[low]

    middle = low + (high - low) // 2

    # Check the right half and get the biggest element in it
    # take the max of all the values on the right side
    # right side is defined as either middle - k to middle or, if middle - k is out of range, we use low to middle
    right_range = forts[middle:min(high, middle+k) + 1]
    biggest_right = right_range[0] if len(right_range) == 1 else max(right_range)

    # Check the left half (same as right side)
    left_range = forts[max(low, middle-k):middle + 1]
    biggest_left = left_range[0] if len(left_range) == 1 else max(left_range)

    # If the middle element is the greatest of its k neighbors, its a strategic location
    if forts[middle] >= biggest_right and forts[middle] >= biggest_left:
        return forts[middle]
    
    # If the righ side has a bigger element, choose that side
    if biggest_right >= biggest_left:
        return findStrategicFort(forts, middle + 1, high, k)

    # If the left side has a bigger element, choose that side
    if biggest_left >= biggest_right:
        return findStrategicFort(forts, low, middle - 1, k)

A = [1,1,2,1,1]
B = [10,9,8,7,6]
C = [6,7,8,9,10]
D = [6,7,8,9]
E = [10,9,8,7]
F = [10,4,1,6,7,1,1,1,3,9,8,4,8,7]
G = [10,24,1,6,17,1,1,14,3,9,12,4,8,7]


print(findStrategicFort(A, 0, len(A) - 1, 3))
print(findStrategicFort(B, 0, len(B) - 1, 3))
print(findStrategicFort(C, 0, len(C) - 1, 3))
print(findStrategicFort(D, 0, len(D) - 1, 3))
print(findStrategicFort(E, 0, len(E) - 1, 3))
print(findStrategicFort(F, 0, len(F) - 1, 3))
print(findStrategicFort(G, 0, len(G) - 1, 3))
