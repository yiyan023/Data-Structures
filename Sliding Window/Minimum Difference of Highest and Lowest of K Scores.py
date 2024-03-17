class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        l = 0
        minDiff = float('inf')

        for r in range(k - 1, len(nums)):
            minDiff = min(minDiff, nums[r] - nums[l])
            l += 1
        
        return minDiff