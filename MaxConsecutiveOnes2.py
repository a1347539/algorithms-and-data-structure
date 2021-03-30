def MaxConsecutiveOnes(A, k):    #with k flip

    low = 0
    high = 0
    _max = 0

    for high in range(len(A)):

        if A[high] == 0:
            k -= 1

        while k < 0:
            if A[low] == 0:
                k += 1
                
            low += 1

        _max = max(_max, high-low+1)

    return _max

A = [1,1,1,0,0,1,0,0,0,1,1]
k = 3

print(MaxConsecutiveOnes(A, k))
