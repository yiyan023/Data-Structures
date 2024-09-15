class MyCircularQueue:


    def __init__(self, k: int):
        # will these items all be numbers, characters?
        # duplicates do not matter, since we are just looking at whether the queue is full (has a length of k)
        # front => is that where the elements first enter in a queue?
        # end => is that where the elements first leave the queue?
        # isEmpty returns true if empty, false if not?
        # isFul returns true if full, false if not?
        # enQueue returns false if the operation was not successful => unsuccessful operation happens when the queue is already full?
        # deQueue also returns false if it was unsuccessful => will be unsuccessful IF the queue is already empty

        # testing functions
        # front => if queue is empty, queue is not empty 
        # rear => if queue is empty, queue is not empty 
        # enQueue => if queue has reached length of k, if queue is less than k 
        # deQueue => if queue is empty, if queue is not empty 
        # isEmpty => if queue is empty, if queue is not empty 
        # isFull => if queue is full, if queue is not full

        self.queue = collections.deque()
        self.val = k

    def enQueue(self, value: int) -> bool:
        if len(self.queue) < self.val:
            self.queue.append(value)
            return True 
        
        return False

    def deQueue(self) -> bool:
        if self.queue:
            self.queue.popleft()
            return True 
        
        return False

    def Front(self) -> int:
        return self.queue[0] if self.queue else -1

    def Rear(self) -> int:
        return self.queue[-1] if self.queue else -1

    def isEmpty(self) -> bool:
        return not self.queue

    def isFull(self) -> bool:
        return len(self.queue) == self.val
