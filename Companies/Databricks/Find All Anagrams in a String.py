class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_freq = Counter(p)
        s_freq = defaultdict(int)
        res = []
        l = 0

        for r in range(len(s)):
            if s[r] not in p_freq:
                while l < r:
                    s_freq[s[l]] -= 1
                    l += 1
                
                l += 1
            
            else:
                s_freq[s[r]] += 1

                while s_freq[s[r]] > p_freq[s[r]]:
                    s_freq[s[l]] -= 1
                    l += 1

                if p_freq == s_freq:
                    res.append(l)
                    s_freq[s[l]] -= 1
                    l += 1
                
        return res
