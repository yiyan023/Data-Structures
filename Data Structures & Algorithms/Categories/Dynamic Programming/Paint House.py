class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [[float('inf') for _ in range(3)] for _ in range(len(costs)) ]
        dp[0] = costs[0]

        for i in range(1, len(dp)):
            dp[i][0] = min(dp[i][0], min(dp[i-1][1], dp[i-1][2]) + costs[i][0])
            dp[i][1] = min(dp[i][1], min(dp[i-1][0], dp[i-1][2]) + costs[i][1])
            dp[i][2] = min(dp[i][2], min(dp[i-1][0], dp[i-1][1]) + costs[i][2])
        
        return min(dp[-1])
