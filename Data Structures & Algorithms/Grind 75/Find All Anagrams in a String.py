class Solution:
    def findAnagrams(self, s, p):
        pCount = {}
        sCount = {}

        if len(p) > len(s): return [] #if the string is initially longer, then there are no solutions

        for i in range(len(p)): #initialize the sliding window
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
        
        res = [0] if pCount == sCount else [] #if these hash maps are equal, set res = [0], otherwise make it empty
        l = 0 #initialize left pointer

        for r in range(len(p), len(s)): #from len(p) to len(s), since we already considered up to len(p)
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1 #shift of sliding window

            if sCount[s[l]] == 0: #if l is equal to zero, then remove it from the hash, can lead to problems
                sCount.pop(s[l]) #if a hash map with a value of 0 still exists, then it will not return true 
            
            l += 1

            if sCount == pCount:
                res.append(l) #append left pointer if they are equal
        
        return res
            