import math 

class Solution:
    def minimizeArrayValue(self, nums):
        maxVal, curSum = 0, 0

        for n in range(len(nums)):
            curSum += nums[n]
            maxVal = max(maxVal, math.ceil(curSum / (n + 1)))
        
        return maxVal