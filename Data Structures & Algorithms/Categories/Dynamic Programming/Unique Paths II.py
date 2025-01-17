class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1]: return 0
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        dp[-1][-1] = 1

        for r in range(len(obstacleGrid)-1,-1,-1):
            for c in range(len(obstacleGrid[0])-1,-1,-1):
                if obstacleGrid[r][c] or dp[r][c]: continue
                right = dp[r][c+1] if c + 1 < len(obstacleGrid[0]) else 0
                down = dp[r+1][c] if r + 1 < len(obstacleGrid) else 0
                dp[r][c] = right + down
        
        return dp[0][0]
