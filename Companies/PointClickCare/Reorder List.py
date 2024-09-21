# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head.next, head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

        cur = slow.next
        new_head = slow.next = None 

        while cur:
            print(cur)
            temp = cur.next
            cur.next = new_head
            new_head = cur
            cur = temp

        first, second = head, new_head
        
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second 
            second.next = temp1 
            first, second = temp1, temp2 # shift nodes
