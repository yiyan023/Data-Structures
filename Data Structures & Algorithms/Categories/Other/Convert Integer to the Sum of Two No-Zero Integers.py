class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        for a in range(1, n):
            if self.no_zero(a) and self.no_zero(n - a):
                return [a, n - a]
    
    def no_zero(self, num: int):
        while num:
            digit = num % 10
            num //= 10

            if not digit:
                return False 
        
        return True
