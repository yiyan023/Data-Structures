class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # perimeter of one unit is equal to 4 - # of neighbours 
        queue = collections.deque()
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def in_grid(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def bfs(r, c):
            visited.add((r, c))
            perimeter = 0

            while queue:
                x, y = queue.popleft()
                edges = 0

                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy

                    if in_grid(new_x, new_y) and grid[new_x][new_y] == 1:
                        edges += 1

                        if (new_x, new_y) not in visited:
                            visited.add((new_x, new_y))
                            queue.append((new_x, new_y))
                
                perimeter += (4 - edges)

            return perimeter

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    return bfs(r, c)
        
        return 0
