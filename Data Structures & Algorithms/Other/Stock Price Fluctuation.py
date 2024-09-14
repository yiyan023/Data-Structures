class StockPrice:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.max_time = 0
        self.stock_hash = {}

    def update(self, timestamp: int, price: int) -> None:
        self.max_time = max(self.max_time, timestamp)
        self.stock_hash[timestamp] = price
        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.stock_hash[self.max_time]

    def maximum(self) -> int:
        price, time = -self.max_heap[0][0], self.max_heap[0][1]

        while self.max_heap and self.stock_hash[time] != price:
            heapq.heappop(self.max_heap)
            price, time = -self.max_heap[0][0], self.max_heap[0][1]
        
        return price

    def minimum(self) -> int:
        price, time = self.min_heap[0][0], self.min_heap[0][1]

        while self.min_heap and self.stock_hash[time] != price:
            heapq.heappop(self.min_heap)
            price, time = self.min_heap[0][0], self.min_heap[0][1]

        return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
