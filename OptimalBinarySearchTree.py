def OptimalBinarySearchTree(keyLen, w):
    C = [[0 for _ in range(keyLen)] for _ in range (keyLen)]
    memo = [[0 for _ in range(keyLen)] for _ in range (keyLen)]
    
    for x in range(keyLen):
        for i in range(keyLen-x):
            j = i + x
            _min = 99999
            for k in range(i, j):
                result = C[i][k] + C[k+1][j] + sum(w[i:j])
                if result < _min:
                    _min = result
                    C[i][j] = result
                    memo[i][j] = k+1
                    
    print(memo)
    return(memo)




keys = [1,2,3,4]
w = [4,2,6,3]
keyLen = len(keys)+1
memo = OptimalBinarySearchTree(keyLen, w)


def OBSTContruct(i, j):
    
    if i == j:
        print('/')
    else:
        root = memo[i][j]
        print(root)
        OBSTContruct(i, root-1)
        OBSTContruct(root, j)

        

i = 0
j = len(w)
OBSTContruct(i, j)
