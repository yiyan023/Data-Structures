class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.next_val = self.iterator.next() if self.iterator.hasNext() else None
        
    def peek(self): 
        return self.next_val
    
    def next(self): 
        temp = self.next_val
        self.next_val = self.iterator.next()
        return temp
    
    def hasNext(self): 
        return self.next_val != None
