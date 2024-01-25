class Solution(object):
    def updateMatrix(self, matrix):
        from collections import deque
        q = deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    q.append((i, j))
                else:
                    matrix[i][j] = float('inf')

        while q:
            x, y = q.popleft() #takes the coordinates from the first thing popped
            for h, v in [(1, 0), (-1, 0), (0, 1), (0, -1)]: #these are the different directions
                newX, newY = x+h, y+v
                if 0<= newX < len(matrix) and 0<= newY< len(matrix[0]) : #bounds
                    if matrix[newX][newY] > matrix[x][y] + 1:
                        matrix[newX][newY] = matrix[x][y] + 1
                        q.append((newX, newY))
                
        return matrix