class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        total = 0

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        for n in range(len(nums) + max(nums)):
            if not freq[n]:
                continue 
            
            diff = freq[n] - 1
            freq[n] -= diff 
            freq[n + 1] += diff
            total += diff
                
        return total
