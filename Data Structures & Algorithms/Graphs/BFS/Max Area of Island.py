class Solution(object):
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxArea = 0

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or (r, c) in visit or grid[r][c] == 0:
                return 0
            visit.add((r,c))
            return 1 + dfs(r+1,c) + dfs(r, c+1) + dfs(r-1, c) + dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxArea = max(maxArea, dfs(r, c))
        
        return maxArea
        