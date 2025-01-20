class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []
        dp.append(triangle[0])

        for i in range(1, len(triangle)):
            cur = []
            for j, val in enumerate(triangle[i]):
                left = dp[i-1][j-1] if j - 1 >=0 else float('inf')
                right = dp[i-1][j] if j < len(dp[i-1]) else float('inf')
                cur.append(min(left, right) + val)
                
            dp.append(cur)
        
        return min(dp[-1])
