class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1

        for coin in coins:
            for i in range(len(dp)):
                if i - coin >= 0:
                    dp[i] += dp[i - coin]
        
        return dp[-1]
