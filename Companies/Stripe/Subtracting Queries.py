class SubrectangleQueries:

    # retrieving values after initialization
    # retrieving values that have been updated => once and more than once

    def __init__(self, rectangle: List[List[int]]):
        self.coords = []
        self.value_hash = {}
        self.rect = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.coords.append((row1, col1, row2, col2))
        self.value_hash[(row1, col1, row2, col2)] = newValue

    def getValue(self, row: int, col: int) -> int:
        i = len(self.coords) - 1

        while i >= 0:
            coor = self.coords[i]

            if coor[0] <= row <= coor[2] and coor[1] <= col <= coor[3]:
                return self.value_hash[(coor[0], coor[1], coor[2], coor[3])]
            
            i -= 1
        
        return self.rect[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
