class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        neighbours = [[] for _ in range(n)]
        res = appleCost.copy()

        for s, e, cost in roads:
            neighbours[s - 1].append((e - 1, cost))
            neighbours[e - 1].append((s - 1, cost))
        
        min_heap = [(cost, city) for city, cost in enumerate(appleCost)]

        while min_heap:
            cost, city = heapq.heappop(min_heap)

            for nei, nei_cost in neighbours[city]:
                if cost + (k + 1) * nei_cost < res[nei]:
                    res[nei] = cost + (k + 1) * nei_cost
                    heapq.heappush(min_heap, (cost + (k + 1) * nei_cost, nei))
        
        return res
