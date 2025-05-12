# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow = slow_cur = head
        fast = fast_cur = head.next 

        while fast_cur and fast_cur.next:
            slow_cur.next = slow_cur.next.next 
            fast_cur.next = fast_cur.next.next 
            slow_cur = slow_cur.next 
            fast_cur = fast_cur.next 
        
        slow_cur.next = fast
        return slow
