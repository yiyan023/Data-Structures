class MyHashSet:
    # can numbers be negative?
    # do I have to account for duplicates
    # can numbers be multiple digits 
    # am i only returning a value for the contains function?

    # 1. adding duplicates 
    # 2. container => value exists in the hash (maybe test negative to make sure?)
    # 3. container => value does not exist in the hash 
    # 4. remove => remove value that exists, 
    # 5. remove => remove value that DNE

    def __init__(self):
        self.hash_set = set()

    def add(self, key: int) -> None:
        self.hash_set.add(key)

    def remove(self, key: int) -> None:
        if key in self.hash_set:
            self.hash_set.remove(key)
        
    def contains(self, key: int) -> bool:
        return key in self.hash_set


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
