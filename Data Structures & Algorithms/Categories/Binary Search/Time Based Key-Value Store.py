class TimeMap:

    def __init__(self):
        # literally just a hash 
        self.keyVal = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyVal:
            self.keyVal[key] = [] # initialize an empty array
        
        self.keyVal[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyVal.get(key, [])

        l, r = 0, len(values) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            
            else:
                r = mid - 1
        
        return res