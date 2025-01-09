class Solution(object):
    def partitionLabels(self, s):
        hash = {}
        res = []

        for i in range(len(s)):
            hash[s[i]] = i # replaces after every occurrence 

        curLen, last = 0, 0
        for i in range(len(s)):
            last = max(last, hash[s[i]])
            curLen += 1
            
            if i == last:
                res.append(i)
                curLen = 0

        return res