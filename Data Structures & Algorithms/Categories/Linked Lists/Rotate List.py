# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow, fast = head, head 
        list_len = 0

        while fast:
            list_len += 1
            slow = fast
            fast = fast.next
        
        # if list is empty or length 1, k modulo is 0, return current result 
        if list_len <= 1 or not k % list_len: return head
        
        rotations = (list_len - 1 - k % list_len)
        dummy = head

        while rotations:
            rotations -= 1
            dummy = dummy.next 
        
        temp = dummy.next
        dummy.next = None 
        slow.next = head 
        return temp
