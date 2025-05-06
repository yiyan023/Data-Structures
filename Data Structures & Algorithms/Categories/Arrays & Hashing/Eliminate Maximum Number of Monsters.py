class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time_heap = []
        time = 0

        for i in range(len(dist)):
            monst_time = dist[i] / speed[i]
            heapq.heappush(time_heap, monst_time)

        while time_heap:
            cur_monst = heapq.heappop(time_heap)

            if cur_monst <= time:
                return time
            
            time += 1

        return time
