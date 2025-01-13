class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = [0] * len(values)
        dp[0] = values[0]
        max_score = 0

        for i in range(1, len(dp)):
            right = values[i] - i
            max_score = max(max_score, dp[i-1] + right) # update max score, current val is right element 
        
            left = values[i] + i # update the max left element value up until this point
            dp[i] = max(dp[i-1], left)
        
        return max_score

