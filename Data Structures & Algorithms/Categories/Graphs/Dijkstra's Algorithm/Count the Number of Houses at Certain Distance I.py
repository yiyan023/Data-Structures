class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        neighbours = [[h-1, h+1] for h in range(n)]
        neighbours.append([n - 1])
        neighbours[1] = [2]
        neighbours[x].append(y)
        neighbours[y].append(x)
        min_costs = []
        res = []

        def dfs(h):
            min_heap = [(0, h)]
            res = [float('inf')] * (n + 1)

            while min_heap:
                path, house = heapq.heappop(min_heap)
                res[house] = min(res[house], path)

                for nei in neighbours[house]:
                    if 1 + res[house] < res[nei]:
                        heapq.heappush(min_heap, (1 + res[house], nei))
            
            return res
        
        for i in range(1, n+ 1):
            min_cost = dfs(i)
            min_costs.append(tuple(min_cost))
        
        freq_hash = Counter(cost for costs in min_costs for cost in costs)
        
        for i in range(1, n+1):
            res.append(freq_hash[i])
        
        return res
