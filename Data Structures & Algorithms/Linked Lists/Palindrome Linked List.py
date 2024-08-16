class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        def reverseList(head):
            prev = None 
            cur = head
            
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur 
                cur = temp
            
            return prev
        
        reverse = reverseList(slow)
        
        while reverse:
            if head.val != reverse.val:
                return False 
            
            head = head.next 
            reverse = reverse.next
        
        return True
