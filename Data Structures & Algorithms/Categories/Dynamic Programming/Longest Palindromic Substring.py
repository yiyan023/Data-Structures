# time -- O(n^2)
class Solution:
    def longestPalindrome(self, s):
        def expand(l, r):
            while (l >= 0 and r < len(s) and s[l] == s[r]): #make sure to do a while loop
                l -= 1
                r += 1
            
            return s[l+1:r]
        
        result = "" #initialize empty string 
        
        for i in range(len(s)):
            odd = expand(i, i)

            if len(odd) > len(result): #make sure to compare lengths not the string itself
                result = odd 
            
            even = expand(i, i + 1)

            if len(even) > len(result):
                result = even 
        
        return result
                


        