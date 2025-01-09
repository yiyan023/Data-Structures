class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) :

            if nums[i] != i+1 and  nums[nums[i]-1]!=nums[i]: # swap only if one of them is not equal 
                    nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
            else:
                i+=1
        
        return [ i+1 for i in range(len(nums)) if nums[i]!=i+1]
