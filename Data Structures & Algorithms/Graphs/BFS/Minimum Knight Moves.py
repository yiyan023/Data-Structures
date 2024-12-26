class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [[2, 1], [1, 2], [-2, 1], [-1, 2], [2, -1], [1, -2], [-2, -1], [-1, -2]]
        queue = collections.deque()
        visited = set()
        queue.append((0, 0))
        steps = 0
        
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if (r, c) == (x, y):
                    return steps

                visited.add((r, c))
                
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    
                    if (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c))
            
            steps += 1
        
