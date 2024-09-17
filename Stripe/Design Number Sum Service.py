class NeighborSum:

    # standard case for adjacentSum => all neighbours are in range & valid for sum 
    # edge case 1 for adjacentSum => top-left vertex only returns sum of right & down values 
    # edge case 2 for adjacentSum => bottom-right vertex only returns sum of left & top values

    # standard case for diagonalSum => all diagonals are in range & valid for sum 
    # edge case 1 for diagonalSum => choose element on right edge that is not vertex, returns sum of left diagonal values 
    # edge case 2 for diagonalSum => choose element on left edge that is not vertex, returns sum of right diagionals

    # appraoch 1: use a hash map to store the relation between a value and its coordinates

    def __init__(self, grid: List[List[int]]):
        self.grid = grid 
        self.coords = {}

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                self.coords[grid[r][c]] = (r, c)

    def adjacentSum(self, value: int) -> int:
        acc = 0
        r, c = self.coords[value]

        acc += self.grid[r-1][c] if r-1 >= 0 else 0
        acc += self.grid[r+1][c] if r+1 < len(self.grid) else 0
        acc += self.grid[r][c-1] if c-1 >= 0 else 0 
        acc += self.grid[r][c+1] if c+1 < len(self.grid[0]) else 0

        return acc

    def diagonalSum(self, value: int) -> int:
        acc = 0
        r, c = self.coords[value]

        acc += self.grid[r-1][c-1] if r-1 >= 0 and c-1 >= 0 else 0
        acc += self.grid[r+1][c+1] if r+1 < len(self.grid) and c+1 < len(self.grid[0]) else 0
        acc += self.grid[r+1][c-1] if c-1 >= 0 and r+1 < len(self.grid) else 0 
        acc += self.grid[r-1 ][c+1] if r-1 >= 0 and c+1 < len(self.grid[0]) else 0

        return acc


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
