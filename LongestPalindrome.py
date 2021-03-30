def LPS(s):
    start = 0
    maxlength = 1
    i = 0    #for iteration
    low = 0    #result
    n = len(s)
    high = n

    if n == 1:
        return s
    
    for x in range(n):
        
        low = x
        high = x + 1
        while low >= 0 and high < n and s[low] == s[high]:
            if high - low + 1 > maxlength:
                start = low
                maxlength = high - low + 1
            low -= 1
            high += 1

        low = x - 1
        high = x + 1
        while low >= 0 and high < n and s[low] == s[high]:

            if high - low + 1 > maxlength:
                start = low
                maxlength = high - low + 1
            low -= 1
            high += 1
    
    return s[start:start + maxlength]



String = "a"
print(LPS(String))
