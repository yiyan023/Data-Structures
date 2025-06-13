class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        min_diff = float('inf')

        for i, time in enumerate(timePoints):
            ah, am = time.split(":")
            bh, bm = timePoints[(i + 1) % len(timePoints)].split(":")

            a = int(ah) * 60 + int(am)
            b = int(bh) * 60 + int(bm)
            d1 = abs(b - a)
            d2 = 24 * 60 - d1

            min_diff = min(min_diff, d1, d2)
        
        return min_diff
