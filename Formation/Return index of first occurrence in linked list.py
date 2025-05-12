def Node:
    self.__init__(self, val, next=None):
    self.val = val
    self.next = next 

def firstIndexInLL(node: Node, target: int) -> int:
    index = 0

    while node:
        if node.val == target:
            return index
        
        index += 1
        node = node.next
    
    return -1

# explore 
# duplicates? 
# empty list?
# negative numbers?
# unsorted? 
# what happens if the target doesn't exist in the list?

# empty list 
# 1 node list (element exists and doesn't exist)
# list with duplicate values of the target (return first)
# list of unique values without target (return -1)
# general cases - duplicate values, target exists, etc. 
# also test the positions -> first, second, last position 

# approach
# 1. iterate through the linked list & check if the current value is equal to the target, if it is, then return the index 
# will keep track using incrementation 
# O(n) time, O(1) space

