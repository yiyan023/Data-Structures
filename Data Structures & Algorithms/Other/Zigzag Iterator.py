class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.i, self.j = 0, 0
        self.v1, self.v2 = v1, v2

    def next(self) -> int:
        if self.i < len(self.v1) and self.i <= self.j or self.j >= len(self.v2):
            cur = self.v1[self.i]
            self.i += 1

        else:
            cur = self.v2[self.j]
            self.j += 1

        return cur

    def hasNext(self) -> bool:
        return self.i < len(self.v1) or self.j < len(self.v2)
