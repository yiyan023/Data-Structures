class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort() #sort the array

        if not nums:
            return nums

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: #if there are duplicates
                continue 
            
            l, r = i + 1, len(nums) - 1 # left & right pointers

            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1
                
                elif threeSum > 0:
                    r -= 1
                
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l] == nums[l-1]: #if the left is a duplicate
                        l += 1
        
        return result
        