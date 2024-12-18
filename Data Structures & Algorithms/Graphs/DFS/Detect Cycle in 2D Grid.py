class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()
        directions = [[1,0], [-1,0], [0, 1], [0,-1]]

        def not_edge(r, c):
            return r >= 0 and c >=0 and r < len(grid) and c < len(grid[0])

        def dfs(r, c, prev, char):
            if (r,c) in seen:
                return True

            visited.add((r, c))
            seen.add((r, c))

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                if not_edge(new_r, new_c) and (not prev or (new_r, new_c) != prev) and grid[new_r][new_c] == char:
                    if dfs(new_r, new_c, (r, c), char):
                        return True
                 
            return False

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited:
                    seen = set()

                    if dfs(r, c, None, grid[r][c]):
                        return True
        
        return False
