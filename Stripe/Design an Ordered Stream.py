class OrderedStream:
    # example 1 => insert returns a value everytime because a value is added to the cell that the ptr is pointing to 
    # example 2 => insert value at index much larger than ptr, then inserting value at ptr (gap in between)
    # example 3 => insert value at index much larger than pointer, then descending until you reach pointer => choices
    #   pointer to mkae a big jump

    def __init__(self, n: int):
        self.stream = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey-1] = value
        self.res = []

        if idKey - 1 == self.ptr:
            while self.ptr < len(self.stream) and self.stream[self.ptr]:
                self.res.append(self.stream[self.ptr])
                self.ptr += 1
        
        return self.res
