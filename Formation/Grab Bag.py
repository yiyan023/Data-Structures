
import random 

class RandomizedSet:
    def __init__(self):
        self.hash_map = {}
        self.arr = []
    
    def insert(self, val):
        if val in self.hash_map:
            return False 
        
        self.hash_map[val] = len(self.arr)
        self.arr.append(val)
        return True
    
    def remove(self, val):
        if val not in self.hash_map:
            return False 
        
        l, r = self.hash_map[val], len(self.arr) - 1

        # swap 
        self.arr[l], self.arr[r] = self.arr[r], self.arr[l]
        self.hash_map[self.arr[l]] = l

        # pop
        self.arr.pop()
        self.hash_map.pop(val)
        return True
    
    def getRandom(self):
        if len(self.arr) > 0:
            return random.choice(self.arr)
        
        return None

random_set = RandomizedSet()
assert random_set.getRandom() == None
assert random_set.insert(1) == True
assert random_set.insert(1) == False
assert random_set.insert(2) == True 
assert random_set.insert(3) == True 
assert random_set.remove(1) == True
assert random_set.arr == [3, 2]
assert random_set.hash_map[3] == 0 # 1's old index
assert random_set.insert(1) == True 
assert random_set.insert(4) == True 
assert random_set.arr == [3, 2, 1, 4]
assert random_set.remove(1) == True 
assert random_set.hash_map[4] == 2
print("Passed all test cases")
