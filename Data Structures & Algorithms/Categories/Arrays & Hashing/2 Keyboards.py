class Solution:
    def minSteps(self, n: int) -> int:
        # number of steps needed up from 1 to n
        ans = 0
        d = 2

        while n > 1:
            while not n % d:
                n //= d
                ans += d
            
            d += 1
        
        return ans
