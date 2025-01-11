class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        
        s_freq = Counter(s)
        palins = 0

        for c in s_freq.keys():
            if s_freq[c] % 2:
                palins += 1
        
        return palins <= k
