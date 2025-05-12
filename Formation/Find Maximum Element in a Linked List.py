# empty case?
# will there be negative values?
# always integers? 
# not sorted? 
# duplicates? 

# empty list 
# list with duplicates 
# list with unique values 
# list with negative + positive values 
# increasing, decreasing, mixed 

# have a variable that stores the max value & updates everytime you iterate through the list 
# when we reach the end of the list, return that value 
# O(n) time, O(1) space 

import sys 

def find_max(node: ListNode) -> int:
    if not node.next:
        return node.val
    
    return max(node.val, find_max(node.next))
