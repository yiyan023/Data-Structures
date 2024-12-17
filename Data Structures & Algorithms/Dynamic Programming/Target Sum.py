class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        new_sum = sum(nums) + target

        if new_sum % 2 != 0 or abs(sum(nums)) < abs(target):
            return 0
        
        target_sum = new_sum // 2

        dp = [0 for _ in range(target_sum + 1)] 
        dp[0] = 1

        for num in nums:
            for curr_sum in range(target_sum, num - 1, -1):
                dp[curr_sum] += dp[curr_sum - num]
        
        return dp[-1]
