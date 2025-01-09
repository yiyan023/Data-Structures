class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        picked = [False] * len(nums)

        def dfs(idx, arr, picked):
            if len(arr) == len(nums):
                res.append(arr)
                return 
            
            for i in range(len(nums)):
                if not picked[i]:
                    picked[i] = True 
                    dfs(i+1, arr + [nums[i]], picked)
                    picked[i] = False

        dfs(0, [], picked)
        return res
