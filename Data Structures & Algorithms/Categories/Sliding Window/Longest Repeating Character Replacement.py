class Solution:
    def characterReplacement(self, s, k):
        count = {} #occurrence of each letter in the substring
        maxLen = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxLen = max(maxLen, count[s[r]]) #max w/o changing string w/ k

            if (r - l + 1) - maxLen > k: # for this approach, you are comparing it with the letter that appears the most frequently, not s[l]
                count[s[l]] -= 1
                l += 1 #shift the window
        
        return r - l + 1