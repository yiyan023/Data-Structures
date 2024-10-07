class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res, cur = "", ""
        s = s.replace("-", "").upper()
        chars = len(s) % k

        for c in s:
            cur += c.upper() if c != "-" else ""

            if chars and not res and len(cur) == chars:
                res += cur + "-"
                cur = ""
            
            if len(cur) == k:
                res += cur + "-"
                cur = ""
        
        return res[:len(res)-1]
