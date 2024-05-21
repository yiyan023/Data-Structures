class Solution(object):
    def maxDistToClosest(self, seats):
        maxDistance = 0

        l = 0
        for r in range(len(seats)):
            if seats[r]:
                if not seats[l]:
                    maxDistance = max(r - l, maxDistance)
                else: 
                    maxDistance = max((r - l) // 2, maxDistance)
                l = r
            elif r == len(seats) - 1 and not seats[r]:
                maxDistance = max(maxDistance, r - l)
    
        return maxDistance
        