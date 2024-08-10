class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        minLen = float('inf')
        ones, l = 0, 0
        result = ""

        for r in range(len(s)):
            if s[r] == "1":
                ones += 1
                
                while ones > k or s[l] == "0":
                    if s[l] == "1":
                        ones -= 1
                    l += 1

                if ones == k and (r - l + 1 < minLen or r - l + 1 == minLen and s[l:r+1] < result):
                        minLen = r - l + 1
                        result = s[l:r+1]

        return result
