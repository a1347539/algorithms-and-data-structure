def LCS(A, B, i, j):
    LCS_memo = {}
    if A[i] == "/" or B[j] == "/":
        return 0
    if A[i] == B[j]:
        return 1+LCS(A, B, i+1, j+1)
    if A[i]!=B[j]:
        if LCS_memo[i][j]:
            return max(LCS(A, B, i+1, j), LCS(A, B, i, j+1))
    

A = [1,3,5,7,9]
B = [1,4,5,6,4,9,"/"]
i = 0
j = 0

print(sum(A[1:5]))
