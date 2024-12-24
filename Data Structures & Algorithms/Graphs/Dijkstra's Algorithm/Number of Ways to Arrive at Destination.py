class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        neighbours = [[] for _ in range(n)]
        min_costs = [float('inf')] * n
        paths = [0] * n
        paths[0] = 1
        min_costs[0] = 0
        min_heap = [(0, 0)]

        for s, e, cost in roads:
            neighbours[s].append((e, cost))
            neighbours[e].append((s, cost))
        
        while min_heap:
            cost, node = heapq.heappop(min_heap)

            if cost > min_costs[node]:
                continue

            for nei, nei_cost in neighbours[node]:
                if min_costs[node] + nei_cost < min_costs[nei]:
                    paths[nei] = paths[node]
                    min_costs[nei] = min_costs[node] + nei_cost
                    heapq.heappush(min_heap, (min_costs[node] + nei_cost, nei))
                
                elif min_costs[node] + nei_cost == min_costs[nei]:
                    paths[nei] += paths[node]
        
        return paths[n-1] % (10**9 + 7)
        
        
