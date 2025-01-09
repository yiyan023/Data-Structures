class Solution(object):
    def generateMatrix(self, n):
        result = [[0] * n for x in range(n)]
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        cur, maxNumber = 2, n ** 2
        r, c, i = 0, 0, 0
        result[0][0] = 1
        
        while cur <= maxNumber:
            dr, dc = directions[i % 4]
            r, c = r + dr, c + dc
            
            while r in range(n) and c in range(n) and not result[r][c]:
                result[r][c] = cur 
                cur += 1
                
                 # condition to switch directions
                if r + dr not in range(n) or c + dc not in range(n) or result[r + dr][c + dc]:
                    break
                
                r, c = r + dr, c + dc
                
            i += 1
        
        return result
        