class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        total = 0
        prefix_sum = {}
        max_len = 0

        for i, num in enumerate(nums):
            total += num 

            if total == k:
                max_len = max(max_len, i + 1)

            if total - k in prefix_sum:
                max_len = max(max_len, i - prefix_sum[total - k])
            
            prefix_sum[total] = i if total not in prefix_sum else min(prefix_sum[total], i)
        
        return max_len
