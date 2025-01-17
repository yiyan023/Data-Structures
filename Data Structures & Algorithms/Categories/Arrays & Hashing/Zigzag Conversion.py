class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [""] * (numRows)
        down = True 
        row_idx = 0

        for c in s:
            rows[row_idx] += c

            if (row_idx + 1 >= numRows and down) or (row_idx - 1 < 0 and not down):
                down = not down
            
            row_idx = row_idx + 1 if down else row_idx - 1

        
        return ''.join(rows)
