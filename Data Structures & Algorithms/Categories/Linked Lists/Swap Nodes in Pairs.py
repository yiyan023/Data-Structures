# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        slow, fast = head, head.next 

        while slow and fast:
            temp = fast.val
            fast.val = slow.val
            slow.val = temp 

            if slow.next:
                slow = slow.next.next
            if fast.next:
                fast = fast.next.next
        
        return head
