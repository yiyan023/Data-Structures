class StockPrice:

    def __init__(self):
        self.stock = defaultdict(int)
        self.maxVal, self.minVal = [], []
        self.latest = 0

    def update(self, timestamp: int, price: int) -> None:
        self.stock[timestamp] = price 
        self.latest = max(self.latest, timestamp)
        heapq.heappush(self.maxVal, (-price, timestamp))
        heapq.heappush(self.minVal, (price, timestamp))

    def current(self) -> int:
        return self.stock[self.latest]

    def maximum(self) -> int: 
        while self.stock[self.maxVal[0][1]] != -self.maxVal[0][0]:
            heapq.heappop(self.maxVal)
        
        return -self.maxVal[0][0]

    def minimum(self) -> int:
        while self.stock[self.minVal[0][1]] != self.minVal[0][0]:
            heapq.heappop(self.minVal)
        
        return self.minVal[0][0]
