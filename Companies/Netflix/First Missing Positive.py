class Solution(object):
    def firstMissingPositive(self, nums):
        def updateNums(num):
            if num < 1 or num > len(nums) or nums[num - 1] == num:
                return
            
            temp = nums[num-1]
            nums[num-1] = num
            updateNums(temp)

        for i, num in enumerate(nums):
            if i + 1 == num:
                continue 
            
            updateNums(num)
        
        for i, num in enumerate(nums):
            if i + 1 != num:
                return i + 1
        
        return len(nums) + 1
