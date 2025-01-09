class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        nums = defaultdict(int)
        result = 0

        # this method, treating the current song as a potential pair
        for t in time:
            r = t % 60

            if not r:
                result += nums[r]
            
            else:
                result += nums[60 - r]
            
            nums[r] += 1
        
        return result
