# empty? 1 node linked list?
# all integers? 
# will there be duplicates?
# negative? 

# test case
# empty, 1-node linked list
# linked list with duplicates + unique values 

# approach
# 1. we want to continue iterating through the array while the next node exists - if it does, we update the value 
# at the end, return this value (will be initialized to -1)
# O(n) time , O(1) space 

# 2. create a two-pointer approach that is initialized to cur.next.next 
# once the fast pointer reaches the end (null), we return the value fo the current slow pointer 
# O(n) time, O(1) space 

# will probably choose the 1st one because the time and space complexity will be the same, but may be cleaner to implement this way (dont' need to check for lists under size of 2)

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def secondToLast(head: Node) -> int:
        res = -1

        while head and head.next:
            res = head.val 
            head = head.next
        
        return res
    
    def secondToLast(head: Node) -> int:
        if not head or not head.next:
            return -1 
        
        while head.next.next:
            head = head.next
        
        return head.val

