class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        island = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        islandNum = 1
        islandSizes = {}
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        max_size = 0

        def isValid(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(r, c):
            if not isValid(r,c) or not grid[r][c] or island[r][c] > 0:
                return 0
            
            island[r][c] = islandNum
            
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] and island[r][c] < 0:
                    islandSize = dfs(r,c)
                    max_size = max(max_size, islandSize)
                    islandSizes[islandNum] = islandSize
                    islandNum += 1
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not grid[r][c]:
                    seen = set()
                    cur_size = 1

                    for dr, dc in directions:
                        new_r, new_c = r + dr, c + dc

                        if isValid(new_r, new_c) and island[new_r][new_c] > 0 and island[new_r][new_c] not in seen:
                            seen.add(island[new_r][new_c])
                            cur_size += islandSizes[island[new_r][new_c]]
                    
                    max_size = max(max_size, cur_size)
        
        return max_size
