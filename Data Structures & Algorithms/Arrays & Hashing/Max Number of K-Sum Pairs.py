class Solution:
    def maxOperations(self, nums, k):
        nums.sort() #sort & use two pointers

        l, r = 0, len(nums) - 1
        tally = 0

        while l < r:
            if nums[l] + nums[r] > k:
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                tally += 1
                r -= 1
                l += 1
        
        return tally
