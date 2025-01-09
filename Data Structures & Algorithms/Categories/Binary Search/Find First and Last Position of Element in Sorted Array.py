class Solution:
    def searchRange(self, nums, target):
        minIndex, maxIndex = -1, -1

        l, r = 0, len(nums) - 1

        # find the first index 
        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] >= target:
                if nums[mid] == target:
                    minIndex = mid 
                
                r = mid - 1

            else:
                l = mid + 1
        
        l, r = 0, len(nums) - 1

        # find the last index
        while l <= r: 
            mid = l + (r - l) // 2

            if nums[mid] <= target:
                if nums[mid] == target:
                    maxIndex = mid 
                
                l = mid + 1

            else:
                r = mid - 1
        
        return [minIndex, maxIndex]