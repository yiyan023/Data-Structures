class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            currentArea = min(height[l], height[r]) * (r - l)
            maxArea = max(maxArea, currentArea)

            # how you move is by comparing heights of the right and left pointer
            if height[r] > height[l]:
                l += 1
            
            else: 
                r -= 1
        
        return maxArea

        