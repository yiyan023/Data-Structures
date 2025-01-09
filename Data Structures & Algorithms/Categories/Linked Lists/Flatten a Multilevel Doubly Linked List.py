# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = head
        end = []

        while head:
            if head.child:
                if head.next:
                    end.append(head.next)
                head.next = head.child 
                head.next.prev = head
                head.child = None 
            
            if end and not head.next:
                cur = end.pop()
                head.next = cur 
                cur.prev = head
            
            head = head.next
  
        return dummy
