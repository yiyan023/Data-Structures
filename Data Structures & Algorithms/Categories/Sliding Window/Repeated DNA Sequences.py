class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        res = set()
        seen = set()

        for i in range(len(s)-9):
            if s[i:i+10] in seen:
                res.add(s[i:i+10])
            
            else:
                seen.add(s[i:i+10])

        return list(res)
