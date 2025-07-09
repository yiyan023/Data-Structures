class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i, j = 0, 0 

        while i < len(start) and start[i] == "_":
            i += 1
            
        while j < len(target) and target[j] == "_":
            j += 1

        while i < len(start) or j < len(target):
            if (i == len(start) and j != len(target)) or (i != len(start) and j == len(target)):
                return False
            
            if start[i] != target[j]:
                return False 
            
            if start[i] == target[j] == "L" and i < j:
                return False 
            
            if start[i] == target[j] == "R" and i > j:
                return False 
            
            i += 1
            j += 1

            while i < len(start) and start[i] == "_":
                i += 1
            
            while j < len(target) and target[j] == "_":
                j += 1
        
        return True
            
