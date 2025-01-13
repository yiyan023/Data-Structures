class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r - 1 >= 0: dp[r][c] = min(dp[r][c], dp[r-1][c] + grid[r][c])
                if c - 1 >= 0: dp[r][c] = min(dp[r][c], dp[r][c-1] + grid[r][c])
            
        return dp[-1][-1]
