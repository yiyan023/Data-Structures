from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for r in range(rows):
            for c in range(cols):
                if not mat[r][c]:
                    queue.append((r, c))
                else:
                    mat[r][c] = float('inf')
        
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                newR, newC = r + dr, c + dc

                if 0<= newR < rows and 0<= newC < cols and mat[newR][newC] > 1 + mat[r][c]:
                    mat[newR][newC] = 1 + mat[r][c]
                    queue.append((newR, newC))
        
        return mat