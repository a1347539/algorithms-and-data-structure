import math
def dac(A, target):
    l = 0
    h = len(A)-1
    while l<=h:
        mid = round((h+l)/2)
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            l = mid + 1
        else:
            h = mid - 1
    return "not found"
        
A = [1,4]
target = 0
print(dac(A, target))
