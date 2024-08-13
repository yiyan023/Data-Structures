class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arrSum = sum(nums) // 2

        if sum(nums) % 2:
            return False 
        
        dp = set()
        dp.add(0)

        for n in nums:
            nextDp= set()

            for v in dp:
                if n + v == arrSum:
                    return True 
                
                # otherwise, add this number to the set, along with its sum with the current values in dp 
                nextDp.add(v)
                nextDp.add(n+v)
            
            dp = nextDp

        return False
