class Solution:
    def largestAltitude(self, gain):
        acc = 0
        maxAlt = float('-inf')

        for num in gain:
            acc += num 
            maxAlt = max(acc, maxAlt)
        
        return max(maxAlt, 0)
        