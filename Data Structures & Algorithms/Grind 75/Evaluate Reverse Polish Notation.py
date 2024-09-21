class Solution:
    def evalRPN(self, tokens):
        stack = []

        for val in tokens:
            if val == "+":
                stack.append(stack.pop() + stack.pop())
            elif val == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif val == "*":
                stack.append(stack.pop() * stack.pop())
            elif val == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(val))
            
        return stack.pop()
        