class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        neighbours = defaultdict(list)
        total_cost = 0
        min_costs = []

        for i, letter in enumerate(original):
            neighbours[ord(letter) - ord('a')].append((ord(changed[i]) - ord('a'), cost[i]))
        
        def dfs(ori):
            min_heap = [(0, ori)]
            res = [float('inf')] * 26

            while min_heap:
                cost, node = heapq.heappop(min_heap)
                res[node] = min(res[node], cost)

                for nei, cost in neighbours[node]:
                    if cost + res[node] < res[nei]:
                        heapq.heappush(min_heap, (cost + res[node], nei))
            
            return res
        
        for i in range(26):
            min_i_costs = dfs(i)
            min_costs.append(min_i_costs)
        
        for i in range(len(source)):
            if source[i] != target[i]:
                min_cost = min_costs[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')]

                if min_cost == float('inf'):
                    return -1 
                
                total_cost += min_cost
        
        return total_cost
        
