# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        _, l1_num = self.addTwoNumbersHelper(l1)
        _, l2_num = self.addTwoNumbersHelper(l2)
        new_num = str(l1_num + l2_num)
        new_head = cur = ListNode(0)

        for c in new_num:
            cur.next = ListNode(int(c))
            cur = cur.next
        
        return new_head.next
    
    def addTwoNumbersHelper(self, lst):
        if not lst.next:
            return (1, lst.val)
        
        mult, val = self.addTwoNumbersHelper(lst.next)
        return (mult * 10, val + mult * 10 * lst.val)
