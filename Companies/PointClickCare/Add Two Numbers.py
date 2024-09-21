class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_list = ListNode(None)
        tail = sum_list
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0 

            total = v1 + v2 + carry 
            carry = total // 10
            sum_list.next = ListNode(total % 10, None)
            sum_list = sum_list.next

            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None
        
        return tail.next
