# is it possible to undo multiple operations at a time 
# can u undo append and backspace? 
# what happens if you backspace on an input array
# will it be all characters (being added to a string? )

# undo multiple times in a row for different commands 
# undo append, backspace 
# do nothing if we undo an empty string
# empty string 
# append, no backspaces 
# backspace on nothing

def simulate_undo(commands: list[str]) -> str:
    # stack for undo history (to sort things in order of redoing most recent)

    # stack to also pop characters when we backspace, we cannot modify specific characters easily in a string 

    history, res = [], []

    for command in commands:
        if command == "backspace":
            if res:
                char = res.pop()
                history.append(f"{command} {char}")
        
        elif command == "undo":
            if history:
                cmd, char = history.pop().split(" ")

                if cmd == "append":
                    res.pop()

                else:
                    res.append(char)
        
        else:
            res.append(command.split(" ")[1])
            history.append(command)
    
    return ''.join(res)

# Test Case 1: Basic operations
commands = ["append a", "append b", "append c", "backspace", "undo"]
result = simulate_undo(commands)
print(result == "abc")

# Test Case 2: Multiple undos
commands = ["append a", "append b", "append c", "backspace", "undo", "undo"]
result = simulate_undo(commands)
print(result == "ab")

# Test Case 3: Empty input
commands = []
result = simulate_undo(commands)
print(result == "")

# Test Case 4: Complex operations
commands = ["append a", "append b", "backspace", "append c", "undo", "append d", "undo", "append e"]
result = simulate_undo(commands)
print(result == "ae")

# Test Case 5: Undo with no history
commands = ["undo"]
result = simulate_undo(commands)
print(result == "")

# Test Case 6: Backspace with empty text
commands = ["backspace"]
result = simulate_undo(commands)
print(result == "")

# Test Case 7: Multiple backspaces
commands = ["append a", "append b", "append c", "backspace", "backspace"]
result = simulate_undo(commands)
print(result == "a")

# Test Case 8: Undo after multiple backspaces
commands = ["append a", "append b", "append c", "backspace", "backspace", "undo", "undo"]
result = simulate_undo(commands)
print(result == "abc")

# Test Case 9: Continuous undos and backspaces
commands = ["append a", "append b", "append c", "undo", "undo", "undo", "backspace", "backspace", "backspace", "append d", "append e", "append f"]
result = simulate_undo(commands)
print(result == "def")
        
        
