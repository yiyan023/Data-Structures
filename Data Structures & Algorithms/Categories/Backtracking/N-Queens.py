class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        
        def backtrack(r, c, grid, queens):
            if r >= n - 1:
                if queens == n:
                    res.append([''.join(row) for row in grid])
                
                return

            def is_possible_queen(r, c):
                return r not in rows and c not in cols and (r-c) not in diag1 and (r+c) not in diag2

            for new_c in range(n):
                if is_possible_queen(r+1,new_c):
                    rows.add(r+1)
                    cols.add(new_c)
                    diag1.add(r+1-new_c)
                    diag2.add(r+1+new_c)
                    grid[r+1][new_c] = "Q"
                    
                    backtrack(r+1, new_c, grid, queens + 1)

                    rows.remove(r+1)
                    cols.remove(new_c)
                    diag1.remove(r+1-new_c)
                    diag2.remove(r+1+new_c)
                    grid[r+1][new_c] = "."
        
        for c in range(n):
            grid = [["." for _ in range(n)] for _ in range(n)]
            rows,cols = set(), set()
            diag1, diag2 = set(), set()

            rows.add(0)
            cols.add(c)
            diag1.add(-c)
            diag2.add(c)
            grid[0][c] = "Q"

            backtrack(0 , c, grid, 1)
        
        return res
