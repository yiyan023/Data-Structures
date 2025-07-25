class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r // 3, c // 3)].add(board[r][c])
        
        def next_values(r, c):
            if c < len(board) - 1:
                return (r, c + 1)
            
            else:
                return (r + 1, 0)
        
        def backtrack(r, c):
            if r >= len(board) or c >= len(board[0]):
                return True
            
            if board[r][c] != ".":
                new_r, new_c = next_values(r, c)
                return backtrack(new_r, new_c)
            
            for num in "123456789":
                if num not in rows[r] and num not in cols[c] and num not in squares[(r // 3, c // 3)]:
                    rows[r].add(num)
                    cols[c].add(num)
                    squares[(r // 3, c // 3)].add(num)
                    board[r][c] = num 
                    
                    new_r, new_c = next_values(r, c)
                    
                    if backtrack(new_r, new_c):
                        return True
                    
                    rows[r].remove(num)
                    cols[c].remove(num)
                    squares[(r // 3, c // 3)].remove(num)
                    board[r][c] = "."
            
            return False
        
        backtrack(0, 0)
        return board
