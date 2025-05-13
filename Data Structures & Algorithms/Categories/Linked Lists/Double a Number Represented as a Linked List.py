# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        carry, new_prod = self.doubleItHelper(head)

        return new_prod if not carry else ListNode(carry, new_prod)
    
    def doubleItHelper(self, head): 
        if not head.next:
            return ((head.val * 2) // 10, ListNode((head.val * 2)  % 10))
        
        carry, digit = self.doubleItHelper(head.next)
        return ((carry + head.val * 2) // 10, ListNode((carry + head.val * 2) % 10, digit))
