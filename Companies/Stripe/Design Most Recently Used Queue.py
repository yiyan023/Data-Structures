class MRUQueue:

    def __init__(self, n: int):
        self.arr = [n for n in range(n+1)]

    def fetch(self, k: int) -> int:
        self.arr.append(self.arr.pop(k))
        return self.arr[-1]
