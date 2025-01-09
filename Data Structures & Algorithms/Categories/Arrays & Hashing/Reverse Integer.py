class Solution(object):
    def reverse(self, x):
        sign = 1
        
        if x < 0:
            sign = -1
        
        newX = str(abs(x))[::-1]
        
        print(newX)
        return sign * int(newX) if (-2) ** 31 <= int(newX) <= 2 ** 31 - 1 else 0
        
