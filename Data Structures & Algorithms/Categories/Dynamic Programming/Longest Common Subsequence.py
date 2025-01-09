class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # check for equality 
        if text1 == text2:
            return len(text1)
        
        dp = [[0 for _ in range(len(text1))] for _ in range(len(text2))]

        for i in range(len(text2)):
            for j in range(len(text1)):
                if text2[i] == text1[j]:
                    dp[i][j] = 1 if i-1 < 0 or j - 1 < 0 else dp[i-1][j-1] + 1
                
                else:
                    prev_turn = dp[i-1][j] if i - 1 >= 0 else 0
                    prev_val = dp[i][j-1] if j - 1 >= 0 else 0
                    dp[i][j] = max(prev_turn, prev_val)
        print(dp)
        return dp[-1][-1]
