class MyHashMap:
    # deals with duplicates 
    # deals with numbers with multiple digits 
    # non-negative integers 

    # put => (1) adding a key that is not already in the hash, (2), updating a key that is in the hash
    # get => (1) retrieving a key that is in the hash, (2) returning -1 for a key that isnt the hash 
    # remove => (1) remove a key if it is in the hash, (2) nothing happens

    def __init__(self):
        self.hash = {}

    def put(self, key: int, value: int) -> None:
        self.hash[key] = value

    def get(self, key: int) -> int:
        return self.hash[key] if key in self.hash else -1

    def remove(self, key: int) -> None:
        if key in self.hash:
            self.hash.pop(key)
