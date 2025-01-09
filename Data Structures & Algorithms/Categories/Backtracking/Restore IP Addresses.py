class Solution:
    def restoreIpAddresses(self, s):
        result = []

        if len(s) > 12:
            return result

        def dfs(i, dots, curS):
            if dots == 4 and i == len(s):
                result.append(curS[:-1])
                return 
            
            if dots > 4:
                return 
            
            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j+1]) <= 255 and (i == j or s[i] != "0"):
                    dfs(j + 1, dots + 1, curS + s[i:j + 1] + ".")
        
        dfs(0, 0, "")
        return result