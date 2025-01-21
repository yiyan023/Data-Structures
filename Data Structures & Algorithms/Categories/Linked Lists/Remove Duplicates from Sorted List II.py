# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        slow = ListNode(0, head)
        dummy = slow
        fast = head 

        while fast:
            visited.add(fast.val)

            if fast.next and fast.next.val in visited:
                while fast and fast.val in visited:
                    fast = fast.next 
                
                slow.next = fast 
            
            else:
                slow = slow.next
                fast = fast.next
        
        return dummy.next
