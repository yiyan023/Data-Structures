class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_hash = defaultdict(list)
        max_sum = float('-inf')

        def digit_sum(num):
            res = 0

            while num:
                res += (num % 10)
                num //= 10
            
            return res
        
        for num in nums:
            cur_sum = digit_sum(num)
            
            if digit_hash[cur_sum]:
                max_sum = max(max_sum, -digit_hash[cur_sum][0] + num)
            
            heapq.heappush(digit_hash[cur_sum], -num)
        
        return max_sum if max_sum != float('-inf') else -1
