class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        cur_prod = 1
        res = 0

        for r, num in enumerate(nums):
            cur_prod *= nums[r]

            while cur_prod >= k and l <= r:
                cur_prod /= nums[l]
                l += 1
            
            res += (r - l + 1)

        return res
