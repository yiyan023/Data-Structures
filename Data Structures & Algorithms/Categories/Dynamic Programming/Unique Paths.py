class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[1] * n for x in range(m)]
        
        for r in range(m):
            for c in range(n):
                if not r or not c:
                    continue 
                
                else:
                    board[r][c] = board[r-1][c] + board[r][c-1]
        
        return board[m-1][n-1]
