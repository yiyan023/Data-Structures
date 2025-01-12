class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = points[0]

        for r in range(1, len(points)):
            next_dp = dp.copy()
            left_max = [0] * len(dp)
            right_max = [0] * len(dp)

            left_max[0] = dp[0]

            for c in range(1, len(left_max)):
                left_max[c] = max(left_max[c - 1] - 1, dp[c])
            
            right_max[-1] = dp[-1]
            for c in range(len(right_max)-2, -1, -1):
                right_max[c] = max(right_max[c + 1] - 1, dp[c])
            
            for c in range(len(next_dp)):
                next_dp[c] = points[r][c] + max(right_max[c], left_max[c])
        
            dp = next_dp
        
        return max(dp)
