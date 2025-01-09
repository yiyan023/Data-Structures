class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        primes = [True] * n
        i = 2

        while (i * i) < n:
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False
            i += 1
        
        return primes.count(True)-2
