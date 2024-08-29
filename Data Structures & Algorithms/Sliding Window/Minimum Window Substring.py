class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, minStr, minLen = 0, "", float('inf')
        tHash, sHash = {}, {}
        
        for c in t:
            tHash[c] = 1 + tHash.get(c, 0)
        
        cur, res = 0, len(tHash)

        for r in range(len(s)):
            if s[r] not in tHash:
                continue 
            
            sHash[s[r]] = 1 + sHash.get(s[r], 0)

            if sHash[s[r]] == tHash[s[r]]:
                cur += 1

            while cur == res:
                if r-l+1 < minLen:
                    minLen = len(s[l:r+1])
                    minStr = s[l:r+1]
                
                if s[l] in sHash:
                    sHash[s[l]] -= 1

                    if sHash[s[l]] < tHash[s[l]]:
                        cur -= 1
                
                l+=1

        return minStr
