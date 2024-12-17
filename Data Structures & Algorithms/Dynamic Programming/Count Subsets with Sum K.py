class Solution:
  def countSubsets(self, num, sum1):
    if sum1 == 0:
      return 1
    
    dp = [0 for _ in range(sum1 + 1)]
    dp[0] = 1

    for n in num:
      for curr_sum in range(sum1, n-1, -1):
        if dp[curr_sum - n]:
          dp[curr_sum] += dp[curr_sum - n]
    
    return dp[-1]
