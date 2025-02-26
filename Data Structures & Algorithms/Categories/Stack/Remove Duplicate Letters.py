class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        idx_dict = {c:i for i, c in enumerate(s)}
        c_set = set()
        stack = []

        for i, c in enumerate(s):
            if c not in c_set:
                while stack and stack[-1] > c and idx_dict[stack[-1]] > i:
                    c_set.remove(stack.pop())
            
                stack.append(c)
                c_set.add(c)
        
        return ''.join(stack)
