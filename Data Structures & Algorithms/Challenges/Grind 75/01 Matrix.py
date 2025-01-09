class Solution(object):
    def updateMatrix(self, matrix):
        from collections import deque
        queue = deque()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                else:
                    matrix[i][j] = float('inf')
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions: #these are the different directions
                newX, newY = x + dx, y + dy
                if 0<= newX < len(matrix) and 0<= newY< len(matrix[0]) :
                    if matrix[newX][newY] > matrix[x][y] + 1:
                        matrix[newX][newY] = matrix[x][y] + 1
                        queue.append((newX, newY))
            
        return matrix
