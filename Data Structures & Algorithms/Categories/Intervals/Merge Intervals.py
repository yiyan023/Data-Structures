class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 0:
            return intervals 
        
        i = 1
        intervals.sort(key=lambda x: x[0]) #make sure to sort the intervals first 
        newInterval = intervals[0]
        result = []

        for interval in intervals:
            if newInterval[1] < interval[0]:
                result.append(newInterval)
                newInterval = interval
            if newInterval[0] <= interval[1]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        result.append(newInterval)
        return result
        
        
        