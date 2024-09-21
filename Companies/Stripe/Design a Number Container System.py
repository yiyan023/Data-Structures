import collections

class NumberContainers:

    # so a number can be the value for multiple indices?
    # are we accounting for negative numbers? 
    # if we run into duplicate indices, we just update the value?

    def __init__(self):
        self.hash = {}
        self.number_indices = collections.defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.hash[index] = number 
        heapq.heappush(self.number_indices[number], index)

    def find(self, number: int) -> int:
        min_heap = self.number_indices[number]

        while min_heap and self.hash[min_heap[0]] != number:
            heapq.heappop(min_heap)
        
        return min_heap[0] if min_heap else -1
