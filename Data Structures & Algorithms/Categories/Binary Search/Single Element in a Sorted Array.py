class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # log n -> implies binary search 
        # odd vs. even? 

        # find the mid & compare the number of elements on each side 
        # if len(nums[:mid]) % 2: go left 
        # otherwise, if the right is odd, go right, etc. 
        # otherwise, that means we found the unique!!

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            
            left = mid >= 1 and nums[mid] == nums[mid-1]
            right = mid + 1 < len(nums) and nums[mid] == nums[mid + 1]

            m1 = mid - 1 if left else mid 
            m2 = mid + 1 if right else mid

            if len(nums[:m1]) % 2:
                r = m1 - 1
            
            elif len(nums[m2+1:]) % 2:
                l = m2 + 1
            
            elif not left or not right:
                return nums[mid]
