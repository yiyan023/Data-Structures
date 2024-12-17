class Solution:
  def solveKnapsack(self, profits, weights, capacity):
    if capacity == 0 or len(profits) == 0:
      return 0
    
    dp = [[0 for _ in range(capacity)] for _ in range(len(profits))]
    
    # populate first row
    for j in range(weights[0]-1, len(dp[0])):
      dp[0][j] = profits[0]
    
    # populate other rows 
    for i in range(1, len(dp)):
      for j in range(len(dp[0])):
        col = profits[i] if j- weights[i] < 0 else dp[i-1][j-weights[i]] + profits[i]
        if j < weights[i] - 1:
          col = 0
        dp[i][j] = max(col, dp[i-1][j])
    
    return dp[-1][-1]
