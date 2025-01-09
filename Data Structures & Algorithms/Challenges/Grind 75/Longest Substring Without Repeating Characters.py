class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charSet = set()
        tally = 0

        for r in range(len(s)):
            while s[r] in charSet: #remove duplicates if they are in a row
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            tally = max(tally, r - l + 1)
        
        return tally


        