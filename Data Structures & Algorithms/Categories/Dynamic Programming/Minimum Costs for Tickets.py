class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf')] * (days[-1] + 1)
        dp[0] = 0
        days_set = set(days)

        for d in range(1, len(dp)):
            if d not in days_set:
                dp[d] = dp[d-1]
            
            else:
                day = dp[max(0, d - 1)] + costs[0]
                week = dp[max(0, d - 7)] + costs[1]
                month = dp[max(0, d - 30)] + costs[2] 
                dp[d] = min(day, week, month)
        
        return dp[-1]
