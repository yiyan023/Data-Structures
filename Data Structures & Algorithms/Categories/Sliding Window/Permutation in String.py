class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1, freq2 = defaultdict(int), defaultdict(int)

        for c in s1:
            freq1[c] = 1 + freq1.get(c, 0)
        
        l = 0

        for r in range(len(s2)):
            freq2[s2[r]] = 1 + freq2.get(s2[r], 0)

            while freq2[s2[r]] > freq1[s2[r]]:
                if s2[l] in freq2:
                    freq2[s2[l]] -= 1

                    if freq2[s2[l]] == 0:
                        freq2.pop(s2[l])
                
                l += 1

            if freq1 == freq2:
                return True 
        
        return False
