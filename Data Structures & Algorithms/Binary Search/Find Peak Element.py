class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        
        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r-l) // 2

            right = mid == len(nums)-1 or nums[mid+1] < nums[mid]
            left = not mid or nums[mid-1] < nums[mid]

            if left and right:
                return mid 
            
            if not left:
                r = mid - 1

            else:
                l = mid + 1
        
        return l
