A = [[0,23,34,4],
     [5,0,34,11],
     [53,9,0,34],
     [12,37,86,0]
     ]

for k in range(len(A)-1):
    for i in range(len(A)-1):
        for j in range(len(A)-1):
            A[i][j] = min(A[i][j], A[i][k]+A[k][j])

print(A)
