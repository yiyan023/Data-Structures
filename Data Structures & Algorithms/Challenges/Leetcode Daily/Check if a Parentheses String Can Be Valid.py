class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        stack = []
        unlocked = []

        for i, c in enumerate(s):
            if locked[i] == "0":
                unlocked.append(i)
            
            elif c == "(":
                stack.append(i)
            
            else:
                if stack: stack.pop()
                elif unlocked: unlocked.pop()
                else:
                    return False 
        
        while stack:
            if not unlocked or stack[-1] > unlocked[-1]:
                return False 
            
            stack.pop()
            unlocked.pop()
        
        return not len(unlocked) % 2
