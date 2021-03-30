def w(i, j):
    if i == 1 or j == 1:
        return 1
    else:
        return (w(i-1, j) + w(i, j-1))

print(w(5,2))
