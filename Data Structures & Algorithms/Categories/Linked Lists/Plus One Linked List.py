# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        carry_over, new_num = self.plusOneHelper(head)
        return new_num if not carry_over else ListNode(carry_over, new_num)
    
    def plusOneHelper(self, head):
        if not head.next:
            return ((head.val + 1) // 10, ListNode((head.val + 1) % 10))
        
        carry_over, next_digit = self.plusOneHelper(head.next)
        return ((carry_over + head.val) // 10, ListNode((carry_over + head.val) % 10, next_digit))
