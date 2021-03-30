def editDistDP(str1, str2, m, n):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            
            if i == 0:
                dp[i][j] = j
                
            elif j == 0:
                dp[i][j] = i

            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] = 1 + min(dp[i-1][j-1],
                                   dp[i][j-1],
                                   dp[i-1][j])
        print(dp)


        
        


str1 = "pon"
str2 = "n"
m = len(str1)
n = len(str2)

editDistDP(str1, str2, m, n)
