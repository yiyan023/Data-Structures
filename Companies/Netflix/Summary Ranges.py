class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        
        res = []
        prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i-1] + 1 != nums[i]:
                res.append(f"{nums[i-1]}" if prev == nums[i-1] else f"{prev}->{nums[i-1]}")
                prev = nums[i]
        
        res.append(f"{nums[-1]}" if prev == nums[-1] else f"{prev}->{nums[-1]}")
        return res
