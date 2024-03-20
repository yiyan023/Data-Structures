class Solution(object):
    def countGoodSubstrings(self, s):
        count = 0
        
        for r in range(len(s) - 2):
            if len(set(s[r:r+3])) == 3:
                count += 1
        
        return count
        