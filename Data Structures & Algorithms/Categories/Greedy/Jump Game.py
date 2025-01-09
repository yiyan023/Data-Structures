class Solution(object):
    def canJump(self, nums):
        p, i = len(nums) - 1, len(nums) - 1

        while i >= 0:
            if nums[i] + i >= p:
                p = i
            
            i -= 1
        
        return p == 0