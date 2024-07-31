class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        arr = []
        minDiff = float('inf')

        for t in timePoints:
            hour, minute = int(t[:2]), int(t[3:5])
            arr.append(hour * 60 + minute)

            if hour < 12:
                arr.append((24 + hour) * 60 + minute)
                
        arr.sort()
        l, r = 0, 1

        while r < len(arr):
            minDiff = min(minDiff, arr[r] - arr[l])
            l, r = l + 1, r + 1
        
        return minDiff
