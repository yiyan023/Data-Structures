from collections import deque

class Solution:
    def orangesRotting(self, grid) -> int:
        # initialization
        if not grid:
            return grid 
        
        q = deque()
        visit = set()
        rows, cols = len(grid), len(grid[0])
        time = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1 
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        while fresh > 0 and q:
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            for i in range(len(q)):
                r,c = q.popleft()
                
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc

                    if newR in range(rows) and newC in range(cols) and (newR, newC) not in visit and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        fresh -= 1
                        q.append((newR, newC))
                
            time += 1
        
        return time if fresh == 0 else -1    