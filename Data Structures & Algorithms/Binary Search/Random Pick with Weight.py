class Solution:

    def __init__(self, w: List[int]):
        # cumulative sums are effective for efficient random sampling in weighted distributions
        self.acc = [0] + list(accumulate(w)) # weight can be represented as an accumulative sum
        self.sum = sum(w)

    def pickIndex(self) -> int:
        return bisect_right(self.acc, randrange(0, self.sum)) - 1
