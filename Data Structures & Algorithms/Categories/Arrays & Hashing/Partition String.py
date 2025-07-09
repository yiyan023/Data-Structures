class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        l = 0
        res = []

        for r in range(1, len(s)):
            if s[l:r] not in seen:
                res.append(s[l:r])
                seen.add(s[l:r])
                l = r

        if l < len(s) and s[l:] not in seen:
            res.append(s[l:])
        
        return res
