class Solution:
    def fib(self, n: int) -> int:
        one, two = 0, 1
        
        for i in range(n):
            temp = one + two
            one = two
            two = temp
        
        return one
