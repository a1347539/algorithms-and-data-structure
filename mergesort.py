def mergeSort(A, B, a, b):
    i = 0
    j = 0
    C = []
    
    while i < a and j < b:
        if A[i] < B[j]:
            C.append(A[i])
            i+=1
        else:
            C.append(B[j])
            j+=1
    for x in range(a-1-i):
        C.append(A[i])
    for y in range(b-1-j):
        C.append(B[j])
    return C

A = [1,23,34,52,54]
B = [2,11,22,43]
a = len(A)
b = len(B)
print(mergeSort(A, B, a, b))
