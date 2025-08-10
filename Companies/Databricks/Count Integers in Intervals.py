import bisect 

class CountIntervals:

    def __init__(self):
        self.intervals = []
        self.total = 0

    def add(self, left: int, right: int) -> None:
        cur = [left, right]
        insert_idx = bisect.bisect_left(self.intervals, cur)

        while insert_idx - 1 >= 0 and left <= self.intervals[insert_idx - 1][1]: # sorts by start, need to readjust based on end
            insert_idx -= 1
        
        removed = 0

        while insert_idx < len(self.intervals) and right >= self.intervals[insert_idx][0]:
            cur[0] = min(cur[0], self.intervals[insert_idx][0])
            cur[1] = max(cur[1], self.intervals[insert_idx][1])
            removed += self.intervals[insert_idx][1] - self.intervals[insert_idx][0] + 1 # will be double counted
            self.intervals.pop(insert_idx)
        
        self.intervals.insert(insert_idx, cur)
        self.total += (cur[1] - cur[0] + 1) - removed
                
    def count(self) -> int:
        return self.total


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()

# create an array that stores a range of intervals 
# add an interval -> need to find a way to merge it to prevent duplicates 
# count the number of integers -> can either be done by storing a variable that indicates number of numbers, or iterate through the interval ranges and add up the numbers 
