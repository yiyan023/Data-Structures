class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        dups = set()
        p = 1
        dups.add(p)

        for _ in range(n):
            p = heapq.heappop(heap)

            for prime in primes:
                if p * prime not in dups:
                    dups.add(p * prime)
                    heapq.heappush(heap, p * prime)
        
        return p
            
