class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        newInterval = intervals[0]

        for interval in intervals:
            if newInterval[1] < interval[0]:
                result.append(newInterval)
                newInterval = interval
            
            # check to make sure there is an overlap
            # checking newInterval[1] <= interval[1] is redundat
            if newInterval[1] <= interval[1]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        result.append(newInterval)
        return result
