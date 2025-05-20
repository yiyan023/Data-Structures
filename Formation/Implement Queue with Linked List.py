class LLNode:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next

class LLQueue:
    def __init__(self):
        node = LLNode(0)
        self.head = node
        self.tail = node 
        self.size = 0

    def enqueue(self, newValue):
        node = LLNode(newValue)
        self.tail.next = node
        self.tail = self.tail.next
        self.size += 1
    
    def dequeue(self):
        if self.size == 0:
            return -1

        temp = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return temp.value

    def getSize(self):
        return self.size
