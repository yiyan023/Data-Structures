class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        directions =[[-1, 0], [1, 0], [0, 1], [0, -1]]
        
        def dfs(i, row, col, cur, visited):
            if cur == word:
                return True

            if i >= len(word):
                return False
            
            found = False

            for dr, dc in directions:
                new_r, new_c = row + dr, col + dc

                if new_r >= 0 and new_r < len(board) and new_c >= 0 and new_c < len(board[0]) and board[new_r][new_c] == word[i] and visited[new_r][new_c] == False:
                    visited[new_r][new_c] = True
                    found = found or dfs(i+1, new_r, new_c, cur + board[new_r][new_c], visited)
                    visited[new_r][new_c] = False
            
            return found

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    visited[r][c] = True
                    
                    if dfs(1, r, c, board[r][c], visited):
                        return True
                    
                    visited[r][c] = False

        return False
