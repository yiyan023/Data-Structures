from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.hash = defaultdict(list)
    
    def get(self, key: str, target: int):
        if not len(self.hash[key]):
            return ""

        l, r = 0, len(self.hash[key]) - 1
        min_value = ""

        while l <= r:
            mid = (l + r) // 2

            time, value = self.hash[key][mid]

            if time <= target:
                min_value = value
                l = mid + 1
            
            else:
                r = mid - 1
            
        return min_value
    
    def set(self, key: str, value: str, timestamp: int):
        self.hash[key].append((timestamp, value))

print("Test Case 1: Basic set and get operations")
tm = TimeMap()
tm.set("foo", "bar", 1)
print(tm.get("foo", 1))
print(tm.get("foo", 0) == "")
print(tm.get("foo", 2) == "bar")

print("Test Case 2: Multiple sets and gets")
tm = TimeMap()
tm.set("foo", "bar1", 1)
tm.set("foo", "bar2", 2)
print(tm.get("foo", 1) == "bar1")
print(tm.get("foo", 2) == "bar2")
print(tm.get("foo", 3) == "bar2")
print(tm.get("foo", 0) == "")

print("Test Case 3: Multiple keys")
tm = TimeMap()
tm.set("foo", "bar", 1)
tm.set("baz", "qux", 2)
print(tm.get("foo", 1) == "bar")
print(tm.get("baz", 2) == "qux")
print(tm.get("baz", 1) == "")

print("Test Case 4: Timestamps before any value was set")
tm = TimeMap()
tm.set("foo", "bar", 5)
print(tm.get("foo", 1) == "")

print("Test Case 5: Timestamps after the last value was set")
tm = TimeMap()
tm.set("foo", "bar", 5)
print(tm.get("foo", 10) == "bar")

print("Test Case 6: Timestamps in between set timestamps")
tm = TimeMap()
tm.set("foo", "bar1", 5)
tm.set("foo", "bar2", 10)
print(tm.get("foo", 7) == "bar1")
print(tm.get("foo", 10) == "bar2")

print("Test Case 7: Setting multiple values at the same timestamp")
tm = TimeMap()
tm.set("foo", "bar1", 5)
tm.set("foo", "bar2", 5)
print(tm.get("foo", 5) == "bar2")

print("Test Case 8: Setting values out of order")
tm = TimeMap()
tm.set("foo", "bar1", 5)
tm.set("foo", "bar2", 10)
print(tm.get("foo", 10) == "bar2")
print(tm.get("foo", 7) == "bar1")

print("Test Case 9: Key that was never set")
tm = TimeMap()
print(tm.get("unknown", 5) == "")

print("Test Case 10: No values set at all")
tm = TimeMap()
print(tm.get("foo", 5) == "")
