class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if k >= len(grid) + len(grid[0]) - 2: # optimization
            return len(grid) + len(grid[0]) - 2
        
        queue = deque()
        queue.append((0,0,k,0))
        visited = set()
        visited.add((0,0,k))
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def is_inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        while queue:
            r, c, cur_k, dist = queue.popleft()

            if (r,c) == (len(grid) - 1, len(grid[0]) - 1):
                return dist

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                if is_inbound(new_r, new_c):
                    block = grid[new_r][new_c]

                    if block and not cur_k:
                        continue 
                    
                    if block and (new_r, new_c, cur_k - 1) not in visited:
                        queue.append((new_r, new_c, cur_k - 1, dist + 1))
                        visited.add((new_r, new_c, cur_k - 1))
                    
                    elif not block and (new_r, new_c, cur_k) not in visited:
                        queue.append((new_r, new_c, cur_k, dist + 1))
                        visited.add((new_r, new_c, cur_k))
        
        return -1
