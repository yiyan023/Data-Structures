class Solution:
    def singleNonDuplicate(self, nums):
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if mid % 2:
                mid -= 1 # odd index will always be the second element in the pair

            if nums[mid] != nums[mid + 1]:
                r = mid
            
            else:
                l = mid + 2 # there are duplicates 
        
        return nums[l]

        