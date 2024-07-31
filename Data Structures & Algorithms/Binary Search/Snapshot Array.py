class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[] for x in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append([val, self.snap_id])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        cur = self.arr[index]

        # can use binary search since snap_id will be sorted in order!
        res, l, r = 0, 0, len(cur) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if cur[mid][1] <= snap_id:
                res = cur[mid][0]
                l = mid + 1
            
            else:
                r = mid - 1
        
        return res
