class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []

        for c in s:
            stack.append(c)

            while len(stack) >= len(part) and ''.join(stack[-len(part):]) == part:
                stack = stack[:-len(part)]
        
        return ''.join(stack)
