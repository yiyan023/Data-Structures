class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        result = ""
        
        for c in s:
            freq[c] = 1 + freq.get(c, 0)
        
        for c in order:
            while c in freq and freq[c]:
                result += c
                freq[c] -= 1
        
        for c in s:
            if c not in order:
                result += c
            
        return result
        
