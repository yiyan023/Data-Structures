# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        c1, c2 = list1, list2

        while a > 1:
            a, b = a - 1, b - 1
            c1 = c1.next 

        c1_copy = c1

        while b:
            b -= 1
            c1_copy = c1_copy.next
        
        c1.next = list2
        c1 = c1.next

        while c2 and c2.next:
            c1 = c1.next
            c2 = c2.next 

        c1.next = c1_copy.next
        return list1
        
        
        
