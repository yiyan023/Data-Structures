class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1

        for num in range(3, n+1):
            for factor in range(1, num):
                dp[num] = max(dp[num], (num - factor) * max(factor, dp[factor]))
        
        return dp[-1]
