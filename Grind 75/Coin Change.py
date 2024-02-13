class Solution:
    def coinChange(self, coins, amount):
        coins.sort()

        dp = [0] + [float('inf')] * amount #initialize the array 

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1) 

        if dp[-1] == float('inf'): return -1 
        else: return dp[-1] #return value stored in last element

        