class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        islands = 0

        def not_edge(r, c):
            return r > 0 and c > 0 and r < len(grid) - 1 and c < len(grid[0]) - 1

        def bfs(r, c):
            visited.add((r, c))
            is_closed = True

            while queue:
                x, y = queue.popleft()

                if not not_edge(x, y):
                    is_closed = False
                
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy

                    if new_x >= 0 and new_y >= 0 and new_x < len(grid) and new_y < len(grid[0]) and (new_x, new_y) not in visited and grid[new_x][new_y] == 0:
                        visited.add((new_x, new_y))
                        queue.append((new_x, new_y))
        
            return is_closed

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c] == 0 and not_edge(r, c):
                    queue.append((r, c))
                    
                    if bfs(r, c):
                        islands += 1

        return islands
        
