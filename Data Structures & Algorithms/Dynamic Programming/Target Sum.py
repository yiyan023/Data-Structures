class Solution:
  def findTargetSubsets(self, num, s):
    # TODO: Write your code here
    adjusted_sum = sum(num) + s

    if adjusted_sum % 2 != 0:
      return 0
    
    target_sum = adjusted_sum // 2
    dp = [0 for _ in range(target_sum + 1)]
    dp[0] = 1

    for n in num:
      for curr_sum in range(target_sum, n - 1, -1):
        dp[curr_sum] += dp[curr_sum - n]
        # print(dp)
    
    return dp[-1]
