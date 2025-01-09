class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        
    def get(self, key):
        if key in self.cache:
            self.cache[key] = self.cache.pop(key) #make sure to put the element back at the end of the hash, MRU
            return self.cache[key]
        
        return -1
        
    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        
        else:
            if not self.capacity:
                self.cache.pop(next(iter(self.cache)))
            
            else:
                self.capacity -= 1
        
        self.cache[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)