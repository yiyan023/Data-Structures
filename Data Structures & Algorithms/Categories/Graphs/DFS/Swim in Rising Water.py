class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        min_heap = [(grid[0][0], 0, 0)]
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = set()
        max_time = 0

        def in_grid(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        while min_heap:
            t, r, c = heapq.heappop(min_heap)

            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return max(max_time, t)

            if (r, c) in visited:
                continue 
            
            visited.add((r, c))
            max_time = max(t, max_time)
            
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                if in_grid(new_r, new_c) and (new_r, new_c) not in visited:
                    heapq.heappush(min_heap, (grid[new_r][new_c], new_r, new_c))
        
                    

