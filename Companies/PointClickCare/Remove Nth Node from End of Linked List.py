# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy= ListNode(None, head)
        tail = dummy
        slow, fast = head, head

        while n:
            fast = fast.next
            n -= 1
        
        while fast:
            dummy = dummy.next
            slow = slow.next
            fast = fast.next 
        
        dummy.next = dummy.next.next
        return tail.next
