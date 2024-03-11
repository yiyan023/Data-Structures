class Solution:
    def checkInclusion(self, s1, s2):
        count1, count2 = {}, {}
        l = 0

        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        
        for r in range(len(s2)):
            if count1 == count2:
                return True 
            
            if s2[r] in count1:
                count2[s2[r]] = 1 + count2.get(s2[r], 0)

            while l < r:
                if s2[r] in count1 and s2[l] in count1 and count2[s2[r]] <= count1[s2[r]]:
                    break
                
                if s2[r] not in count1:
                    if s2[l] in count1: 
                        count2[s2[l]] -= 1

                elif count2[s2[r]] > count1[s2[r]] and s2[l] in count1: 
                    count2[s2[l]] -= 1

                if s2[l] in count2 and count2[s2[l]] == 0:
                    count2.pop(s2[l])
                        
                l += 1

        return count1 == count2