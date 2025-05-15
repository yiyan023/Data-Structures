# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        cur = head

        while cur:
            length += 1
            cur = cur.next 
        
        cur_len, remain = length // k, length % k 
        res = []
        cur = head 

        for _ in range(k):
            max_len = cur_len + 1 if remain > 0 else cur_len

            while cur and max_len > 1:
                cur = cur.next 
                max_len -= 1
            
            temp = cur.next if cur else None 
            if cur: cur.next = None
            res.append(head)
            head = cur = temp 
            remain -= 1
        
        return res
