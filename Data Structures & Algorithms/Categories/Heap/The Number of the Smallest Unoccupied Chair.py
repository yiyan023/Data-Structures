class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target_start, target_end = times[targetFriend]
        min_heap = []
        seats = []

        new_times = [[times[i][0], times[i][1], i] for i in range(len(times))]
        new_times.sort()

        for s, e, i in new_times:
            if s > target_start:
                continue
            
            while min_heap and min_heap[0][0] <= s:
                _, seat = heapq.heappop(min_heap)
                heapq.heappush(seats, seat)

            if i == targetFriend:
                return heapq.heappop(seats) if seats else len(min_heap)
            
            if seats:
                heapq.heappush(min_heap, (e, heapq.heappop(seats)))
                
            else:
                heapq.heappush(min_heap, (e, len(min_heap)))
