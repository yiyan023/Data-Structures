class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        heap = []
        heapq.heappush(heap, intervals[0][1])

        for s, e in intervals[1:]:
            if s >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, e)
        
        return len(heap)
