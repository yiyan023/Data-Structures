class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head 
        
        index = 1
        cur, new_head = head, None  
        l, r, temp = None, None, None

        while cur:
            if index + 1 == left:
                l = cur
                cur = cur.next 
            
            elif left <= index <= right:
                if index == left:
                    r = cur
                
                temp = cur.next 
                cur.next = new_head
                new_head = cur
                cur = temp 

            else:
                cur = cur.next 
            
            index += 1
        
        if l:
            l.next = new_head
        
        if r:
            r.next = temp
        
        return head if left > 1 else new_head
