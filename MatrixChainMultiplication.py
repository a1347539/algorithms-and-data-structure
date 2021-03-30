def MatrixChainMultiplication(d, i, j): #naive
    if i == j:
        return 0

    _min = 999999
    
    for k in range(i, j): 
      
        count = (MatrixChainMultiplication(d, i, k)  
             + MatrixChainMultiplication(d, k+1, j) 
                   + d[i-1] * d[k] * d[j]) 
  
        if count < _min: 
            _min = count;
            
    print(_min)
    
def matrixChainOrder1(p, n):
    m = [[0 for x in range(n)]for x in range(n)]
    s = [[0 for x in range(n)]for x in range(n)]
    _min = 9999
    
    for i in range (n):
        for j in range (n):
            i = 0
            for k in range (i, j):
                
                result = m[i][k]+m[k+1][j]+arr[i]*arr[k+1]*arr[j+1]
                print(m[i][k], "+", m[k+1][j], "+", arr[i], arr[k+1], arr[j+1])
                
                if result < _min:
                    _min = result
                    m[i][j] = result
                    s[i][j] = k
                i+=1
            _min = 9999
                    
    

    
    print(m)
    return m[1][-1]
    



def matrixChainOrder(p, n):
    m = [[0 for x in range(n)]for x in range(n)]
    s = [[0 for x in range(n)]for x in range(n)]
    
    for d in range (1, n-1):
        for i in range (1, n-d):
            j = i + d

            _min = 9999
            for k in range (i, j):
                result = m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                print(m[i][k], "+", m[k+1][j], "+", p[i-1], p[k], p[j], result)
                
                
                if result < _min:
                    _min = result
                    m[i][j] = result
                    s[i][j] = k
            
        print()
    

    
    print(m)
    print(s)
    return m[1][-1]
    
arr = [3,2,4,2,5]
n = len(arr)
print(matrixChainOrder(arr, n))








































