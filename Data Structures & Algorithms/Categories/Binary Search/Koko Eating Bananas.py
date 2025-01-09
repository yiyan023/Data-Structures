import math

class Solution:
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)

        while l <= r:
            mid = l + (r - l) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / mid)
            
            if hours > h:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return l