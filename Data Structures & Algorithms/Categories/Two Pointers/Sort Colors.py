class Solution(object):
    def sortColors(self, nums):
        l, r = 0, len(nums) - 1
        i = 0

        while i <= r:
            if not nums[i]:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            
            if nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                i -= 1
            
            i += 1
        
        