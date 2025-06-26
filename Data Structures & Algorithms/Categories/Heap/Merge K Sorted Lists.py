# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        res = ListNode(0)
        dummy = res

        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(min_heap, (lst.val, i))
        
        while min_heap:
            val, idx = heapq.heappop(min_heap)
            res.next = ListNode(val)
            res = res.next

            if lists[idx].next:
                lists[idx] = lists[idx].next
                heapq.heappush(min_heap, (lists[idx].val, idx))

        return dummy.next
            
    
