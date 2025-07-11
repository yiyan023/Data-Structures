class MaxStack:

    def __init__(self):
        self.set = set()
        self.max_heap = []
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.set.add((x, len(self.stack)))
        heapq.heappush(self.max_heap, (-x, -len(self.stack)))

    def pop(self) -> int:
        while self.stack and (self.stack[-1], len(self.stack)) not in self.set:
            self.stack.pop()

        cur = self.stack.pop() if self.stack else -1
        self.set.remove((cur, len(self.stack)+1))
        return cur
        

    def top(self) -> int:
        while self.stack and (self.stack[-1], len(self.stack)) not in self.set:
            self.stack.pop()
        
        return self.stack[-1] if self.stack else -1

    def peekMax(self) -> int:
        while self.max_heap and (-self.max_heap[0][0], -self.max_heap[0][1]) not in self.set:
            heapq.heappop(self.max_heap)
        
        return -self.max_heap[0][0] if self.max_heap else -1

    def popMax(self) -> int:
        while self.max_heap and (-self.max_heap[0][0], -self.max_heap[0][1]) not in self.set:
            heapq.heappop(self.max_heap)
        
        max_val, idx = heapq.heappop(self.max_heap) if self.max_heap else (-1, -1)
        self.set.remove((-max_val, -idx))
        return -max_val
    
    # 5 1 5
        



# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
