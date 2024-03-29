from collections import heapq

class Solution:
    def getOrder(self, tasks):
        result = []
        heap1, heap2 = [], []
        time = 1

        for i, (e, p) in enumerate(tasks):
            heapq.heappush(heap1, [e, p, i])
        
        while heap1 or heap2:
            while heap1 and heap1[0][0] <= time:
                cur = heapq.heappop(heap1)
                newOrder = [cur[1], cur[2], cur[0]]
                heapq.heappush(heap2, newOrder)

            if not heap2:
                time = heap1[0][0]
            else:
                cur = heapq.heappop(heap2)
                time += cur[0]
                result.append(cur[1])
        
        return result


