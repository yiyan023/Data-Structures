class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [0] * (n + 1)
        dests = [[] for _ in range(n + 1)]

        for s, e, t in rides:
            dests[e].append((s, t))
        
        for i in range(1, n+1):
            for s, t in dests[i]:
                dp[i] = max(dp[i], dp[s] + (i - s + t))
            
            dp[i] = max(dp[i], dp[i-1])
        
        return dp[-1]
