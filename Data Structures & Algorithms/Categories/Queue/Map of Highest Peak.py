class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = collections.deque()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for r in range(len(isWater)):
            for c in range(len(isWater[0])):
                if not isWater[r][c]:
                    isWater[r][c]= float('inf')
                
                else:
                    isWater[r][c] = 0
                    queue.append((r, c))
        
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                if 0 <= new_r < len(isWater) and 0 <= new_c < len(isWater[0]) and isWater[new_r][new_c]:
                    if isWater[new_r][new_c] > isWater[r][c] + 1:
                        isWater[new_r][new_c] = isWater[r][c] + 1
                        queue.append((new_r, new_c))
        
        return isWater
