class Solution:
    def numIslands(self, grid):
        # initialization 
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        from collections import deque 
        visit = set() 
        island = 0 # number of islands

        # implement BFS
        def bfs(r, c):
            queue = deque()
            visit.add((r, c))
            queue.append((r, c))
            
            while queue:
                r, c = queue.popleft() 
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc 
                    
                    if newR in range(rows) and newC in range(cols) and (newR, newC) not in visit and grid[newR][newC] == "1":
                        visit.add((newR,newC))
                        queue.append((newR,newC))

        # finding the number of islands 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r,c)
                    island += 1

        return island
                