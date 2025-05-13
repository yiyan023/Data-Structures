# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur, length = head, 0
        new_idx = {}

        while cur: 
            new_idx[length] = cur.val # store the old index 
            length += 1
            cur = cur.next 

        idx = 0
        cur = head 

        while cur:
            prev_index = (idx - k) % length # calculate the new one with reverse engineering 
            cur.val = new_idx[prev_index]
            idx += 1
            cur = cur.next
        
        return head
