class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp =[0 for _ in range(high + 1)]

        for i in range(1, len(dp)):
            if i - zero >= 0: dp[i] = (dp[i] + 1 + dp[i - zero]) % (10 ** 9 + 7)
            if i - one >= 0: dp[i] = (dp[i]+ 1 + dp[i - one]) % (10 ** 9 + 7)
        
        return (dp[high] - dp[low - 1]) % (10 ** 9 + 7)
