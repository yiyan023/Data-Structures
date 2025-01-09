class Solution(object):
    def totalFruit(self, fruits):
        freq = {}
        l = 0
        maxFruit, curFruit = 0, 0
        
        for r in range(len(fruits)):
            if len(freq) == 2 and fruits[r] not in freq:
                while len(freq) == 2:
                    freq[fruits[l]] -= 1
                    curFruit -= 1
                    
                    if not freq[fruits[l]]:
                        freq.pop(fruits[l])
                    
                    l += 1
            
            freq[fruits[r]] = 1 + freq.get(fruits[r], 0)
            curFruit += 1
            maxFruit = max(maxFruit, curFruit)
        
        return maxFruit
                
                    
                    
                
