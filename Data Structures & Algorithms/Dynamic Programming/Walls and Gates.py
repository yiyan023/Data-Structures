class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs should use a queue!
        queue= collections.deque()
        visit = set();
        row, col = len(grid), len(grid[0])
        directions = [[-1, 0], [1,0], [0,-1], [0,1]]

        for r in range(row):
            for c in range(col):
                if not grid[r][c]:
                    visit.add((r, c))
                    queue.append((r, c))
        
        dist = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist

                for dr, dc in directions:
                    if r + dr in range(row) and c + dc in range(col) and (r+dr, c+dc) not in visit and grid[r+dr][c+dc] != -1:
                        queue.append((r+dr, c+dc))
                        visit.add((r+dr, c+dc))
            
            dist += 1
