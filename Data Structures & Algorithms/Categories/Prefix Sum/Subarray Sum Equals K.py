class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq_hash = defaultdict(int)
        freq_hash[0] = 1
        acc = 0
        res = 0

        for num in nums:
            acc += num

            if acc - k in freq_hash:
                res += freq_hash[acc-k]
            
            freq_hash[acc] += 1
        
        return res
