class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-count for count in freq.values()]
        heapq.heapify(heap)
        queue = collections.deque()
        time = 0

        while heap or queue:
            if heap:
                cur = heapq.heappop(heap)
                if cur + 1:
                    queue.append((cur+1, time + n))
            time += 1

            if queue and queue[0][1] < time:
                heapq.heappush(heap, queue.popleft()[0])
        
        return time
