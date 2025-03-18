class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n-1)
        l = 0
        res = ""

        for r in range(len(prev)):
            if prev[r] != prev[l]:
                res += str(r-l) + prev[l]
                l = r
        
        res += str(len(prev) - l) + prev[l]
        return res
