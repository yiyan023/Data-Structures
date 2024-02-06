class Solution:
    def countSubstrings(self, s):

        def expand(l, r):
            tally = 0
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                tally += 1
            
            return tally
        
        total = 0

        for i in range(len(s)):
            odd = expand(i, i)
            total += odd

            even = expand(i, i+1)
            total += even
        
        return total

        