class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3:
            return n
        
        mod = 10**9 + 7
        dp = [0] * n
        dp[0], dp[1], dp[2] = 1, 2, 5

        for i in range(3, len(dp)):
            dp[i] = (2 * dp[i-1] + dp[i-3]) % mod
        
        return dp[-1]
