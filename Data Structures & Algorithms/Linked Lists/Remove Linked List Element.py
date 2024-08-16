class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = head
        tail = dummy 

        while dummy:
            while dummy.next and dummy.next.val == val:
                dummy.next = dummy.next.next
            
            dummy = dummy.next
        
        return tail if not tail or tail.val != val else tail.next
