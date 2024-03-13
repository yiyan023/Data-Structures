# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        count = 0
        dummy, right = ListNode(0, head), head 
        #we need to create a new linked list with a first node of 0
        # this is because otherwise, the tail will point to the value we want to delete instead of the one before it
        tail = dummy
        
        # initialize position of right pointer
        while count < n:
            right = right.next 
            count += 1
        
        # increment until you reach the node before the one we want to remove 
        while right:
            tail = tail.next 
            right = right.next 
        
        #skip over it
        tail.next = tail.next.next

        # return the dummy
        return dummy.next

        