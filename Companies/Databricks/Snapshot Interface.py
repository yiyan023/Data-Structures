class SnapshotSet:
    def __init__(self):
        self.snap_set = set()

    def add(self, e):
        self.snap_set.add(e)

    def remove(self, e):
        self.snap_set.remove(e)

    def contains(self, e) -> bool:
        return e in self.snap_set

    def iterator(self) -> iter:
        """
        Returns an iterator over a snapshot of the set's elements at the time this method is called.
        """
        return iter(self.snap_set.copy())

s = SnapshotSet()
s.add(5)
s.add(2)
s.add(8)
s.remove(5)

it = s.iterator()  # Snapshot taken now: contains 2 and 8

s.add(1)
print(s.contains(2))  # True
s.remove(2)
print(s.contains(2))  # False

print(list(it))  # Output: [2, 8] (order not guaranteed)
