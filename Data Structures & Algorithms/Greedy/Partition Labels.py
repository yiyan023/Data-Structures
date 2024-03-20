class Solution(object):
    def partitionLabels(self, s):
        freq = {}
        result = []
        charSet = set()

        for c in s:
            freq[c] = 1 + freq.get(c, 0)
        
        p = 0

        for i in range(len(s)):
            if len(charSet) == 0 and i - p > 0:
                result.append(i - p)
                p = i
            
            charSet.add(s[i])   
            freq[s[i]] -= 1
            
            if freq[s[i]] == 0:
                charSet.remove(s[i])
        
        result.append(len(s) - p)
        return result