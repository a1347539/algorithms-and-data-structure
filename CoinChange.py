def CoinChange(coins, amount, remain):
    dict = {}
    
    for coin in coins[::-1]:
         dict[coin] = amount//coin
         amount = amount%coin
            
    print(dict)




coins = [1,2,5]

amount = 150

remain = 0

CoinChange(coins, amount, remain)
