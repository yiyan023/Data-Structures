class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)
        res = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    rows[r] += 1
                    cols[c] += 1
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] and (rows[r] > 1 or cols[c] > 1):
                    res += 1
        
        return res
