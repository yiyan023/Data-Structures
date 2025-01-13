class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1: 
            return n

        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        squares = math.floor(n ** 0.5)

        for num in range(1, len(dp)):
            for s in range(1, squares + 1):
                if s <= num:
                    dp[num] = min(dp[num], dp[num - s ** 2] + 1)

        return dp[-1]
