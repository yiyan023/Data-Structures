# explore
# can numbers be negative? (yes)
# can there be an empty/non-existent linked list case? (return 1)
# does it have to increase by 1 each time? 
# if everything is consecutive, are we returning the next value in the sequence? 

# only integers?

# test cases
# empty case (return 1)
# consecutive sequence (return next available number) - same as testing with 1 node linked list 
# starting at negative, 0, positive number with missing value in different locations on the linked list 

# brainstorm: 
# 1. get the first value of the head & increment it by 1 every time you traverse through the linked list 
# O(n) time, O(1) space

# pseudocode 
# if the list is empty, return 1 
# otherwise, set the initial value to the (head's value + 1) & increment the linked list pointer 
# if its not equal to this value, then return it
# every iteration, increment 

class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

def findMissing(head: Node) -> int:
    if not head:
        return 1
    
    cur = head 

    while cur.next:
        if cur.val + 1 != cur.next.val:
            return cur.val + 1
        
        cur = cur.next
    
    return cur.val + 1

    # can also just check side by side values and check to make sure that .next exists 
