# solution with for loops (slightly faster)
class Solution:
    def productExceptSelf(self, nums):
        prefix = 1
        suffix = 1
        forwardArr = []
        backwardArr = []
        result = []

        for num in nums:
            forwardArr.append(prefix)
            prefix *= num
        
        for num in nums[::-1]:
            backwardArr.append(suffix)
            suffix *= num
        
        backArray = backwardArr[::-1]

        for i in range(len(nums)):
            result.append(forwardArr[i] * backArray[i])
        
        return result

#solution with while loop (my original)
class Solution:
    def productExceptSelf(self, nums):
        prefix = 1
        suffix = 1
        l, r = 0, len(nums) - 1
        prefArr = []
        sufArr = []
        result = []

        while l < len(nums):
            if l > 0:
                prefix *= nums[l-1]
            
            prefArr.append(prefix)
            l += 1
        
        while r >= 0:
            if r < len(nums)-1:
                suffix *= nums[r+1]
            
            sufArr.append(suffix)
            r -= 1
        
        for i in range(len(nums)):
            result.append(prefArr[i] * sufArr[len(nums) - i - 1])

        return result
        



        
        
        



        
        