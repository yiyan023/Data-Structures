def remove_invalid_parentheses(s: str) -> list[str]:
    # need a backtrack function that will choose if we are going to include the current character 

    # use dfs -> keep track of the current string + index (if we reach the length of s, return the string if the length is even)

    # if the current character is open, add it 

    # if the current character is close, don't add it 
    # also backtrack and add it if the number of close is less than the number of opens 

    res = set()

    def backtrack(i, string, open_num, close_num):
        if i >= len(s):
            if open_num == close_num:
                res.add(string)
            
            return 
        
        if s[i] == "(":
            backtrack(i+1, string + s[i], open_num + 1, close_num)
        
        elif s[i] == ")":
            backtrack(i+1, string, open_num, close_num)

            if close_num < open_num:
                backtrack(i+1, string + s[i], open_num, close_num + 1)
        
        else:
            backtrack(i+1, string + s[i], open_num, close_num)
    
    backtrack(0, "", 0, 0)
    return list(res) if res else [""]

example = "()())()"
print(remove_invalid_parentheses(example))

def equal_lists(a,b):
    return sorted(a)==sorted(b)

assert equal_lists(remove_invalid_parentheses("()())()"), ["()()()","(())()"])
assert equal_lists(remove_invalid_parentheses("(a)())()"), ["(a)()()","(a())()"])
assert equal_lists(remove_invalid_parentheses(")("), [""])

print("passed")
