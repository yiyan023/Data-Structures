class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(height):
            diff = 0

            while stack and height[stack[-1]] <= h:
                idx = stack.pop()

                res += (i - idx - 1) * (height[idx] - diff)
                diff = height[idx]
            
            if stack:
                res += (i - stack[-1] - 1) * (h - diff)
            
            stack.append(i)  

        return res
