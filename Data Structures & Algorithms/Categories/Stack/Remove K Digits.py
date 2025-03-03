class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for c in num:
            while k and stack and int(stack[-1]) > int(c):
                stack.pop()
                k -= 1
            
            if not stack and c == "0":
                continue 
            
            stack.append(c)
        
        return ''.join(stack)[:len(stack)-k] if k < len(stack) and stack else "0"
