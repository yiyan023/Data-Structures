class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 1, 1
        count = 1

        while i < len(nums):
            if nums[i-1] == nums[i]:
                count += 1

                if count > 2:
                    i += 1
                    continue # only increment j if count is less than 2 for current i 
                    
            else:
                count = 1 # found new i -> reset the counter 
            
            nums[j] = nums[i]
            i += 1
            j += 1 

        return j
