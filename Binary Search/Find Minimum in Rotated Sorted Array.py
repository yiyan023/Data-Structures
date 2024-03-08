class Solution:
    def findMin(self, nums):
        # find middle & compare to the end
        # middle is less than, we look at left half 
        # middle is greater than the left half, we look at the right side 
        # compare to current min?

        minVal = float('inf')
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] < minVal:
                minVal = nums[mid]
            
            if nums[mid] < nums[r]:
                r = mid - 1
            
            else:
                l = mid + 1
        
        return minVal