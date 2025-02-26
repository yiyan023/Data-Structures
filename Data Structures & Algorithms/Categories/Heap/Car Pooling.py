class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda x: x[1])
        heap = []
        passengers = 0

        for p, s, e in trips:
            while heap and heap[0][0] <= s:
                passengers -= heapq.heappop(heap)[-1]

            passengers += p

            if passengers > capacity:
                return False 

            heapq.heappush(heap, (e, s, p))     

        return True    
