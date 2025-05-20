# no commands case?
# endif or else without if? 
# case sensitive? 
# invalid inputs?

# endif/elseif without if, including keyword is not if
# if and endif do not pair up 
# elseif follows else (false)
# functional case - empty, 1 layer, multiple layers 


def vbNesting(controlFlow: list[str]) -> int:
    # 1. stack -> to check the previous value for invalid examples 
    # 2. also good to check that there are if statements before an endif 
    # time complexity: O(n)
    # space complexity: O(n)

    # general framework 
    # stack -> everytime you run into an endif, we will pop from the stack if it exists until stack[-1] is "if" or if stack doesnt exist 
    # if stack[-1] DNE, return -1, otherwise, pop it from the stack 

    # if action is "if", just add it to the stack 
    # if the action is else: return -1 if stack is empty, otherwise, add it to the stack 
    # if the action is elseif: return -1 if stack is empty or stack[-1] is else 
    # otherwise, add itto the stack 

    # return whether the stack is empty or not 

    stack = []
    cur, res = 1, -1

    for cmd in controlFlow:
        if cmd == "if":
            stack.append((cmd, cur))
            cur += 1
        
        elif cmd == "else" or cmd == "elseif":
            if not stack or stack[-1][0] == "else":
                return -1
            
            stack.append((cmd, cur))
        
        else:
            while stack and stack[-1][0] != "if":
                stack.pop()
            
            if not stack: 
                return -1
            
            string, depth = stack.pop()
            res = max(res, depth)
            cur -= 1
    
    return res

print(vbNesting(["if"]) == -1)
print(vbNesting(["endif"]) ==  -1)
print(vbNesting(["if", "endif"]) == 1)
print(vbNesting(["if", "if", "if", "endif", "endif", "endif"]) == 3)
print(vbNesting(["if", "if", "if", "endif", "endif", "if", "endif", "endif"]) == 3)
print(vbNesting(["if", "else", "endif"]) == 1)
print(vbNesting(["if", "endif", "if", "endif"]) == 1)
print(vbNesting(["if", "if", "endif", "endif"]) == 2)
print(vbNesting(["else"]) == -1)
print(vbNesting(["endif", "if"]) == -1)
print(vbNesting(["if", "else", "if", "endif", "endif"]) == 2)
print(vbNesting(["if", "endif", "if", "elseif", "else", "endif", "endif"]) == -1)
print(vbNesting(["if", "elseif", "elseif", "elseif", "endif"]) == 1)
print(vbNesting(["if", "elseif", "else", "endif"]) == 1)
print(vbNesting(["if", "if", "elseif", "else", "endif", "endif"]) == 2)
print(vbNesting(["if", "endif", "if", "elseif", "else", "endif"]) == 1)
print(vbNesting(["if", "else", "elseif", "endif"]) == -1)
print(vbNesting(["if", "else", "else", "endif"]) == -1)
