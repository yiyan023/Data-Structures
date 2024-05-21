class Solution:
    def solve(self, board):
        visit = set()
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if (r, c) in visit or r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == "X":
                return 
            
            visit.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visit:
                    board[r][c] = "X"
        
        return board
