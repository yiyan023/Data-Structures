class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        sum = 0
        
        i = 0
        
        while i < len(nums):
            sum += nums[i]
            i += 2
        
        return sum
