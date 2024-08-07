class RandomizedSet:

    def __init__(self):
        self.randomSet = set()
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.randomSet:
            return False 
        
        self.randomSet.add(val)
        self.array.append(val)
        return True 

    def remove(self, val: int) -> bool:
        if val not in self.randomSet:
            return False 
        
        self.randomSet.remove(val)
        self.array.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
