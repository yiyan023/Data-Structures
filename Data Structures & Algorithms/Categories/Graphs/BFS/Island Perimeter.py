class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
    
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
    
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:  # If the cell is land
                # Check all four directions
                # Up
                    if i == 0 or grid[i - 1][j] == 0:
                        perimeter += 1
                # Down
                    if i == rows - 1 or grid[i + 1][j] == 0:
                        perimeter += 1
                # Left
                    if j == 0 or grid[i][j - 1] == 0:
                        perimeter += 1
                # Right
                    if j == cols - 1 or grid[i][j + 1] == 0:
                        perimeter += 1
    
        return perimeter
