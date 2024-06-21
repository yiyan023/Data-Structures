class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        visit = set()
        r, c, i = 0, 0, 0 
        row, col = len(matrix), len(matrix[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for j in range(row * col):
            dr, dc = directions[i % 4]

            while r in range(row) and c in range(col) and (r, c) not in visit:
                result.append(matrix[r][c])
                visit.add((r, c))

                if r + dr not in range(row) or c + dc not in range(col) or (r + dr, c + dc) in visit:
                    newR, newC = directions[(i + 1) % 4]
                    r, c = r + newR, c + newC
                    break
                
                r, c = r + dr, c + dc
            
            i += 1
        
        return result
