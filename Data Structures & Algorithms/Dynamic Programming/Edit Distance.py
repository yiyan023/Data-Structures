class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) > len(word2):
            word1, word2 = word1, word2
        
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        
        for i in range(len(word1), -1, -1):
            for j in range(len(word2), -1, -1):
                valid_w1, valid_w2 = i < len(word1), j < len(word2)

                if valid_w1 and valid_w2:
                    if word1[i] == word2[j]:
                        dp[i][j] = dp[i+1][j+1]
                    
                    else:
                        dp[i][j] = min(1 + dp[i+1][j], 1 + dp[i][j+1], 1 + dp[i+1][j+1])
                    
                elif valid_w1:
                    dp[i][j] = 1 + dp[i+1][j]
                
                elif valid_w2:
                    dp[i][j] = 1 + dp[i][j+1]
        
        return dp[0][0]
                    
