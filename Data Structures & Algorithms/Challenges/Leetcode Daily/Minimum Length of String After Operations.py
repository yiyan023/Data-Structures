class Solution:
    def minimumLength(self, s: str) -> int:
        s_freq = Counter(s)
        res = 0
        
        for c in s_freq:
            if s_freq[c] % 2:
                res += 1
            
            else:
                res += 2
        
        return res
