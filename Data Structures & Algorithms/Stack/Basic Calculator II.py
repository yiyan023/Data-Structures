class Solution:
    def calculate(self, s: str) -> int:
        stack, cur, op = [], "", "+"
        s = s.replace(" ", "")

        for c in s + ".": # to apply the final operation?
            if c.isnumeric():
                cur += c
            else:
                if op == "-":
                    stack.append(-int(cur))
                elif op == "+":
                    stack.append(int(cur))
                elif op == "*":
                    stack.append(stack.pop() * int(cur))
                elif op == "/":
                    stack.append(int(stack.pop() / int(cur)))
                
                cur, op = "", c
        return sum(stack)
