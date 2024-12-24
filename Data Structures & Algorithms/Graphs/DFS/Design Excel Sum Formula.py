class Excel:

    def convert(self, alphabet):
        return ord(alphabet)-ord('A')

    def split_colrow(self, cell):
        col=self.convert(cell[:1])
        row=int(cell[1:])
        return (row, col)

    def process_sum(self, numbers):
        total_sum = 0
        for number in numbers:
            cells = number.split(':')

            if len(cells) == 1:
                row,col = self.split_colrow(cells[0])
                val = self.sheet[row][col] 
                total_sum += self.process_sum(val) if type(val) == list else val
            
            else:
                # Case #2: range of cells
                start_row, start_col = self.split_colrow(cells[0])
                end_row, end_col = self.split_colrow(cells[1])
                for row in range(start_row, end_row+1):
                    for col in range(start_col, end_col+1):
                        val = self.sheet[row][col]
                        total_sum += self.process_sum(val) if type(val) == list else val
        
        return total_sum

    def __init__(self, height: int, width: str):
        self.sheet = [[0 for _ in range(self.convert(width)+1)] for _ in range(height+1)]

    def set(self, row: int, column: str, val: int) -> None:
        self.sheet[row][self.convert(column)] = val

    def get(self, row: int, column: str) -> int:
        val = self.sheet[row][self.convert(column)]

        if type(val) == list:
            return self.process_sum(val)
        
        return val
    
    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        # print(self.sheet)
        total_sum = self.process_sum(numbers)
        self.sheet[row][self.convert(column)] = numbers
        return total_sum
        


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
