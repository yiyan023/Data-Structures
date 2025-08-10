import bisect 

class SnapshotArray:

    def __init__(self, length: int):
        self.length = length 
        self.arr = defaultdict(list)
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        insert_idx = bisect.bisect_right(self.arr[index], (snap_id, float('inf'))) - 1
        return self.arr[index][insert_idx][1] if 0 <= insert_idx < len(self.arr[index]) else 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
