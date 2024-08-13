class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arrSum = sum(nums) // 2

        if sum(nums) % 2:
            return False 
        
        dp = set()
        dp.add(0)

        for i in range(len(nums)-1,-1,-1):
            nextDp= set()

            for v in dp:
                if nums[i] + v == arrSum:
                    return True 
                
                # otherwise, add this number to the set, along with its sum with the current values in dp 
                nextDp.add(v)
                nextDp.add(nums[i]+v)
            
            dp = nextDp

        return False
