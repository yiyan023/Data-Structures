class MyCircularDeque:
    # maxmimum k => is it possible that k is zero?
    # if k is full, we don't input into the queue/
    # if empty, we don't remove

    def __init__(self, k: int):
        self.queue = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue = [value] + self.queue
            return True
        
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue.append(value)
            return True
        
        return False

    def deleteFront(self) -> bool:
        if self.queue:
            self.queue.pop(0)
            return True
        
        return False

    def deleteLast(self) -> bool:
        if self.queue:
            self.queue.pop(-1)
            return True
        
        return False

    def getFront(self) -> int:
        return self.queue[0] if self.queue else -1

    def getRear(self) -> int:
        return self.queue[-1] if self.queue else -1

    def isEmpty(self) -> bool:
        return not self.queue

    def isFull(self) -> bool:
        return len(self.queue) == self.k
