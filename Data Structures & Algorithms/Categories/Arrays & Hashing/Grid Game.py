class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        max_path = float('inf')
        top_sum = sum(grid[0])
        bottom_sum = 0

        for i in range(len(grid[0])):
            top_sum -= grid[0][i]
            max_path = min(max(top_sum, bottom_sum), max_path)
            bottom_sum += grid[1][i]
        
        return max_path
