class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        l = 0
        res = []

        for r in range(len(nums)):
            if nums[r] - nums[l] > k or (r - l) >= 3:
                if (r - l) < 3:
                    return []

                res.append(nums[l:r])
                l = r
        
        if l == len(nums) - 3:
            res.append(nums[l:])
        
        return res
