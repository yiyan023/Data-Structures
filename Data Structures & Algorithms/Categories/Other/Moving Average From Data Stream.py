class MovingAverage:

    def __init__(self, size: int):
        self.acc = 0
        self.arr = []
        self.len = size

    def next(self, val: int) -> float:
        self.acc += val 
        self.arr.append(val)

        if len(self.arr) > self.len:
            self.acc -= self.arr.pop(0)

        return self.acc / min(len(self.arr), self.len)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
