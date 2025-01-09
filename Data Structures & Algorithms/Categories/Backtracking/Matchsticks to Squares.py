class Solution:
    def makesquare(self, matchsticks) -> bool:
        length = sum(matchsticks) // 4
        sides = [0] * 4

        if length != sum(matchsticks) / 4:
            return False 
        
        matchsticks.sort(reverse = True)
        
        def dfs(i):
            if i == len(matchsticks):
                return True # made it to the end 
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]

                    if dfs(i + 1):
                        return True
                    
                    sides[j] -= matchsticks[i] 
            
            return False
        
        return dfs(0)