class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        res = [0] * len(heights)

        for i in range(len(heights)-1, -1, -1):
            sees = 0

            while stack:
                if heights[i] <= stack[-1]:
                    sees += 1
                    res[i] = sees
                    break
                
                stack.pop()
                sees += 1
            
            stack.append(heights[i])
            res[i] = sees
        
        return res
