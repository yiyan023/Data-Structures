class Solution:
    def isValidSudoku(self, board):
        # go through each element in a row
        for row in board:
            numSet = set()

            for num in row:
                if num in numSet and num != '.':
                    return False
                else:
                    numSet.add(num)
        
        #columns
        for i in range(len(board)):
            numSet = set()

            for col in board:
                if col[i] in numSet and col[i] != '.':
                    return False
                else:
                    numSet.add(col[i])

        # 3x3 grid
        for i in range(3):
            for l in range(3):
                numSet = set()

                for j in range(3):
                    for k in range(3):
                        curPos = board[3 * i + j][3 * l + k] 
                        if curPos in numSet and curPos != '.':
                            return False
                        else:
                            numSet.add(curPos)

        return True
    
import collections

class Solution:
    def isValidSudoku(self, board):
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sqrs = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.' and (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in sqrs[(r // 3, c // 3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sqrs[(r // 3, c // 3)].add(board[r][c])
        
        return True