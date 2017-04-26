def changes(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for j in range(coin, amount + 1):
            ways[j] += ways[j - coin]
    return ways[amount]
 
print( changes(32, [1,2,3,4,5,6,7,8,9,10,11,12,13]) )
