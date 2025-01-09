class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # set of immutable sets (frozenset)
        res = set()
        visited = set()
        queue = collections.deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def in_grid(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def bfs(r, c):
            translated_island = set()
            visited.add((r, c))

            while queue:
                x, y = queue.popleft()
                translated_island.add((x - init_r, y - init_c))

                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy

                    if in_grid(new_x, new_y) and grid[new_x][new_y] == 1 and (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        queue.append((new_x, new_y))  
            
            return translated_island

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == 1:
                    queue.append((r, c))
                    init_r = r
                    init_c = c
                    res.add(frozenset(bfs(r,c)))
        
        return len(res)
