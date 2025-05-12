# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack, res = [], []
        cur = head
        index = 0

        while cur:
            while stack and stack[-1][0] < cur.val:
                _, i = stack.pop()
                res[i] = cur.val 
            
            stack.append((cur.val, index))
            res.append(0)
            index += 1
            cur = cur.next
        
        return res
