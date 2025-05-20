# explore
# clarification: when a call is released and there are other operators that were added previously, do those have prioritity?
# what happens when you receive a call with no operators? is that possible?
# are all operators and alls unique? 
# can there be no commands (result is an empty array?)

# test cases
# add operatators and match with a call 
# release calls when there are no operators left in the queue 
# release calls when calls are underway 
# release calls when there are operators left in the queue
# empty case 
# no operators available 

# approach
# 1. queue 
# first in, first out (priority for operators )
# when we release a call, we add the operator back to the queue 
# time complexity: O(n)
# space complexity: O(n)

import collections

def process_call_center_actions(actions: list[tuple]) -> list:
    op_queue, call_queue = collections.deque(), collections.deque()
    res = []

    for cmd, actionId in actions:
        if cmd == "add_operator" or cmd == "release_operator": 
            op_queue.append(actionId)
        
        else:
            # if queue is not empty 
            if call_queue or not op_queue:
                call_queue.append(actionId)
            
            if op_queue: 
                call = call_queue.popleft() if call_queue else actionId
                res.append((call, op_queue.popleft()))
    
    while call_queue and op_queue:
        res.append((call_queue.popleft(), op_queue.popleft()))
    
    return res

# Test Case 1: No calls received
actions = [
    ("add_operator", "A"),
    ("add_operator", "B")
]
result = process_call_center_actions(actions)
print(result == [])

# Test Case 2: No operators available
actions = [
    ("receive_call", "1"),
    ("receive_call", "2"),
    ("receive_call", "3")
]
result = process_call_center_actions(actions)
print(result == [])

# Test Case 3: Multiple operators and calls, no releases
actions = [
    ("add_operator", "A"),
    ("add_operator", "B"),
    ("receive_call", "1"),
    ("receive_call", "2"),
    ("receive_call", "3"),
    ("receive_call", "4")
]
result = process_call_center_actions(actions)
print(result == [('1', 'A'), ('2', 'B')])

# Test Case 4: Alternating adding operators and receiving calls
actions = [
    ("add_operator", "A"),
    ("receive_call", "1"),
    ("add_operator", "B"),
    ("receive_call", "2"),
    ("add_operator", "C"),
    ("receive_call", "3")
]
result = process_call_center_actions(actions)
print(result == [('1', 'A'), ('2', 'B'), ('3', 'C')])

# Test Case 5: Complex Operation with releases
actions = [
    ("add_operator", "A"),
    ("add_operator", "B"),
    ("receive_call", "1"),
    ("receive_call", "2"),
    ("release_operator", "A"),
    ("receive_call", "3"),
    ("release_operator", "B"),
    ("receive_call", "4"),
    ("receive_call", "5"),
    ("receive_call", "6"),
    ("release_operator", "A"),
    ("release_operator", "B")
]
result = process_call_center_actions(actions)
print(result == [('1', 'A'), ('2', 'B'), ('3', 'A'), ('4', 'B'), ('5', 'A'), ('6', 'B')])

# Test Case 6: Releasing operators after calls
actions = [
    ("add_operator", "A"),
    ("add_operator", "B"),
    ("receive_call", "1"),
    ("receive_call", "2"),
    ("release_operator", "A"),
    ("release_operator", "B"),
    ("receive_call", "3"),
    ("receive_call", "4"),
]
result = process_call_center_actions(actions)
print(result == [('1', 'A'), ('2', 'B'), ('3', 'A'), ('4', 'B')])

# Test Case 7: Releasing operators without any calls
actions = [
    ("add_operator", "A"),
    ("add_operator", "B"),
    ("release_operator", "A"),
    ("release_operator", "B")
]
result = process_call_center_actions(actions)
print(result == [])

# Test Case 8: Releasing operators while calls are waiting
actions = [
    ("receive_call", "1"),
    ("receive_call", "2"),
    ("add_operator", "A"),
    ("add_operator", "B"),
    ("release_operator", "A"),
    ("receive_call", "3"),
    ("release_operator", "B"),
    ("receive_call", "4")
]
result = process_call_center_actions(actions)
print(result == [('1', 'A'), ('2', 'B'), ('3', 'A'), ('4', 'B')])
