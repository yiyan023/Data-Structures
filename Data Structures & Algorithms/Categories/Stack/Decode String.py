class Solution(object):
    def decodeString(self, s):
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                string, num = "", ""

                while stack[-1] != "[":
                    string = stack.pop(-1) + string
                
                stack.pop(-1)

                while stack and stack[-1].isnumeric():
                    num = stack.pop(-1) + num
                
                stack.append(int(num) * string)
        
        return ''.join(stack)
        
