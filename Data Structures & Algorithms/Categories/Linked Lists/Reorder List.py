# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second list 
        second = slow.next 
        prev, slow.next = None, None 

        while second:
            temp = second.next 
            second.next = prev
            prev = second 
            second = temp

        # merge the two lists 
        one, two = head, prev

        while two: #the second list will be greater than or equal to the first list 
            temp1, temp2 = one.next, two.next 
            one.next = two 
            two.next = temp1 
            one, two = temp1, temp2 # shift the pointers