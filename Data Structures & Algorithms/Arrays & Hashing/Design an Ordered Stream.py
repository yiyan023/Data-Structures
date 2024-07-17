class OrderedStream:

    def __init__(self, n: int):
        self.stream = [""] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value
        self.result = []

        while self.ptr in range(len(self.stream)) and self.stream[self.ptr] != "":
            self.result.append(self.stream[self.ptr])
            self.ptr += 1
        
        return self.result
