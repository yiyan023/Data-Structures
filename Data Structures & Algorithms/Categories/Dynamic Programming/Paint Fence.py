class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1: return k
        if n == 2: return k ** 2

        dp = [0] * (n + 1)
        dp[1] = k
        dp[2] = k ** 2

        for i in range(3, len(dp)):
            dp[i] = (dp[i-1]+ dp[i-2]) * (k-1) 
        
        return dp[-1]
