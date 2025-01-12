class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        max_reach = [0] * len(nums)
        max_reach[-1] = len(nums) - 1
        res = []

        for i in range(len(nums)-2,-1,-1):
            if nums[i+1] % 2 != nums[i] % 2:
                max_reach[i] = max_reach[i+1]
            
            else:
                max_reach[i] = i

        for s, e in queries:
            res.append(max_reach[s] >= e)

        return res
