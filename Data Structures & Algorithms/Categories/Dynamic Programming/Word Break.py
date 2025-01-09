class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            for word in wordDict:
                if i - len(word)+1 >= 0 and dp[i - len(word)+1] and s[i-len(word)+1:i+1] == word:
                    dp[i+1] = True 
                
                if dp[i+1]:
                    break # no need to look at other words
        
        return dp[-1]
