class Solution(object):
    def subsets(self, nums):
        res = []

        def dfs(i, cur):
            if i >= len(nums):
                res.append(cur) # only append at the end
                return 
            
            dfs(i + 1, cur + [nums[i]])
            dfs(i + 1, cur)

        dfs(0, [])
        return res        