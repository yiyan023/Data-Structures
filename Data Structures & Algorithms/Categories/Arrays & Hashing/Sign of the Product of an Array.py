class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negative = 0

        for num in nums:
            if not num:
                return 0
            
            if num < 0:
                negative += 1
        
        return -1 if negative % 2 else 1
