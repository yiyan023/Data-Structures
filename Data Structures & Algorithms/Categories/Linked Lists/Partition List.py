# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before, after = ListNode(0), ListNode(0)
        before_cur, after_cur = before, after 
        cur = head

        while cur:
            if cur.val < x:
                before_cur.next = ListNode(cur.val)
                before_cur = before_cur.next 
            
            else:
                after_cur.next = ListNode(cur.val)
                after_cur = after_cur.next 
            
            cur = cur.next 
        
        before_cur.next = after.next 
        return before.next
