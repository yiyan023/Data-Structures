class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub_set = set()

        def backtrack(i, arr):
            if i >= len(nums):
                if tuple(arr) not in sub_set:
                    res.append(arr)
                    sub_set.add(tuple(arr))
                return
            
            backtrack(i+1, arr)
            backtrack(i+1, arr + [nums[i]])
        
        nums.sort()
        backtrack(0, [])
        return res
