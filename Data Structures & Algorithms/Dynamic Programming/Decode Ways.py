class Solution:
    def numDecodings(self, s):
        if s[0] == '0': return 0
        dp = [0] * (len(s)+1)
        dp[0] = 1

        for i in range(1, len(s) + 1):
            if s[i - 1] != '0': # first you check for the single digit
                dp[i] += dp[i - 1]
            
            if i > 1 and 10 <= int(s[i-2:i]) <= 26: #then you check if the number as the last digit of a two digit numberxdsc
                dp[i] += dp[i - 2]
        
        return dp[len(s)]


        