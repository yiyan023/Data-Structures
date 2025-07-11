class AllOne:

    def __init__(self):
        self.hash_map = defaultdict(int)
        self.min_heap = []
        self.max_heap = []

    def inc(self, key: str) -> None:
        self.hash_map[key] += 1
        heapq.heappush(self.min_heap, (self.hash_map[key], key))
        heapq.heappush(self.max_heap, (-self.hash_map[key], key))

    def dec(self, key: str) -> None:
        self.hash_map[key] -= 1

        if not self.hash_map[key]:
            return 
        
        heapq.heappush(self.min_heap, (self.hash_map[key], key))
        heapq.heappush(self.max_heap, (-self.hash_map[key], key))

    def getMaxKey(self) -> str:
        while self.max_heap and self.hash_map[self.max_heap[0][1]] != -self.max_heap[0][0]:
            heapq.heappop(self.max_heap)
        
        return self.max_heap[0][1] if self.max_heap else ""

    def getMinKey(self) -> str:
        while self.min_heap and self.hash_map[self.min_heap[0][1]] != self.min_heap[0][0]:
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0][1] if self.min_heap else ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
