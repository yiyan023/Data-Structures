from collections import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        visit = set()
        signals = [[] for x in range(n + 1)]
        minTime = 0
        minHeap = [(0, k)]

        for s, f, t in times:
            signals[s].append((f, t))
        
        while minHeap:
            t1, d = heapq.heappop(minHeap)
            if d not in visit:
                visit.add(d)
                minTime = t1 # update the time, it will be in increasing order according to the heap

                for f, t2 in signals[d]:
                    if f not in visit:
                        heapq.heappush(minHeap, (t1 + t2, f))
        
        return minTime if len(visit) == n else -1

