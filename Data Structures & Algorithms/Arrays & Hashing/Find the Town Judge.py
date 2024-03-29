from collections import defaultdict

class Solution(object):
    def findJudge(self, n, trust):
        trusts = defaultdict(int)
        trusted = defaultdict(int)
        
        for a, b in trust:
            trusts[a] += 1
            trusted[b] += 1
        
        for i in range(1, n + 1):
            if trusts[i] == 0 and trusted[i] == n - 1:
                return i
        
        return -1