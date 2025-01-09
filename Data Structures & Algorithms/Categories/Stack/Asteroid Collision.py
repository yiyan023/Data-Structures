class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            addCur = True
            cur = a

            while stack and cur < 0 and cur * stack[-1] < 0:
                prev = stack.pop()

                if abs(prev) >= abs(cur):
                    if abs(prev) > abs(cur):
                        stack.append(prev)
                    addCur = False
                    break
            
            if addCur:
                stack.append(cur)
        
        return stack
