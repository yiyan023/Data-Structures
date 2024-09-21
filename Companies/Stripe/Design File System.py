class FileSystem:
    # can we create the path based on the parent directory of another path?
    # if /leet/code exists, can we call /leet/call ?
    # assuming that all inputs are valid?
    # cannot add a path if the parent directories dne? 

    # finding a path that exists [/leet/code, /leet], /leet => return value 
    # finding a path that DNE [/leet/code, /leet], /leet/call => return -1
    # return the parent path of one of the paths [/leet/code, /leet], /leet => return value
    # create a valid path, where parent exists [/leet], /leet/code => true
    # create an invalid path, parent DNE [/leet], /late/call => false
    # invalid path, some parent directories match, but not call, [/leet/code/hard], /leet/code/medium/q1 => return False
    # checking for invalid inputs => "", "/", return False
    # trying to create a path that already exists, [/leet/code], /leet/code => False

    def __init__(self):
         self.values = {}

    def createPath(self, path: str, value: int) -> bool:
        if not path or path == "/" or path in self.values:
            return False
        
        parent_path = path.rsplit("/", 1)[0]
        
        if not parent_path or parent_path in self.values:
            self.values[path] = value
            return True
        
        return False

    def get(self, path: str) -> int:
        return self.values[path] if path in self.values else -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
