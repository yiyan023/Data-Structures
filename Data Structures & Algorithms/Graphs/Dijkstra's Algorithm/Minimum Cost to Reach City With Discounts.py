class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        queue = collections.deque() # cost, city, discounts used 
        queue.append((0, 0, 0))
        neighbours = [[] for _ in range(n)]
        res = [[float('inf') for _ in range(discounts + 1)] for _ in range(n)]
        res[0][0] = 0

        for s, e, w in highways:
            neighbours[s].append((e, w))
            neighbours[e].append((s, w))

        while queue:
            cost, city, dis = queue.popleft()

            if cost > res[city][dis]:
                continue

            for nei, nei_cost in neighbours[city]:
                if res[city][dis] + nei_cost < res[nei][dis]:
                    res[nei][dis] = res[city][dis] + nei_cost
                    queue.append((res[city][dis] + nei_cost, nei, dis))
                
                if dis < discounts and res[city][dis] + nei_cost // 2 < res[nei][dis + 1]:
                    res[nei][dis + 1] = res[city][dis] + nei_cost // 2 
                    queue.append((res[city][dis] + nei_cost // 2, nei, dis + 1))
            
        min_cost = min(res[n-1])
        return min_cost if min_cost != float('inf') else -1


