class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visit = set()

        def dfs(r,c, i):
            if i == len(word):
                return True
            
            if (r not in range(row) or c not in range(col) or board[r][c] != word[i] or (r,c) in visit):
                return False

            visit.add((r,c))

            res = (dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r+1, c, i+1) or dfs(r, c-1, i+1))

            visit.remove((r,c))
            return res
            
        for r in range(row):
            for c in range(col):
                if dfs(r,c,0): 
                    return True
        
        return False
