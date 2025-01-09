class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cur, result = "", ""
        stack = []
        
        for i in range(len(s)):
            cur += s[i]
            
            if s[i] == "(":
                stack.append(s[i])
            
            else:
                stack.pop(-1)
                
                if not stack:
                    result += cur[1:-1]
                    cur = ""
        
        return result
