class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pi, ni = 0, 1
        res = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                res[pi] = nums[i]
                pi += 2
            
            else:
                res[ni] = nums[i]
                ni += 2
        
        return res
