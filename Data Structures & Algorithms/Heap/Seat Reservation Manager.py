from collections import heapq

class SeatManager:

    def __init__(self, n: int):
        self.n = 0
        self.notReserved= []

    def reserve(self) -> int:
        if not self.notReserved:
            self.n += 1
            return self.n
    
        return heapq.heappop(self.notReserved)

    def unreserve(self, seatNumber: int) -> None:
        if self.n == seatNumber:
            self.n -= 1
        else:
            heapq.heappush(self.notReserved, seatNumber)
        
# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)