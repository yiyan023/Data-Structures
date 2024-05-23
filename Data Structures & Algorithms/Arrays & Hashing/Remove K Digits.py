class Solution(object):
    def removeKdigits(self, num, k):
        if len(num) <= k:
            return "0"
        
        stack = []
        for i in num:
            while k and stack and stack[-1] > i:
                k -= 1
                stack.pop()
            stack.append(i)
        
        while k:
            stack.pop()
            k -= 1
        
        return ''.join(stack).lstrip('0') or '0'
