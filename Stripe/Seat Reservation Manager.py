class SeatManager:
    # reserve the smallest seats in order without unreserving => ascending consecutive numbers 1, 2, 3, 4 etc 
    # unreserving a set and making sure the next reservation reserves that one instead of the next conseutive number

    def __init__(self, n: int):
        self.seat = 1
        self.unreserved = set()

    def reserve(self) -> int:
        if self.unreserved:
            val = min(self.unreserved)
            self.unreserved.remove(val)
            return val
        
        self.seat += 1
        return self.seat - 1

    def unreserve(self, seatNumber: int) -> None:
        self.unreserved.add(seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
