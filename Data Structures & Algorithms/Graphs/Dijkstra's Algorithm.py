class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        to_n= [float('inf')] * (n + 1)
        neighbours = defaultdict(list)
        min_heap = [(0, n)]
        MOD = 10**9 + 7

        for s, e, w in edges:
            neighbours[s].append((e, w))
            neighbours[e].append((s, w))
        
        while min_heap:
            dist, node = heapq.heappop(min_heap)

            if dist < to_n[node]:
                to_n[node] = dist 

                for nei, w in neighbours[node]:
                    heapq.heappush(min_heap, (w + dist, nei))
       
        @lru_cache(None)
        def dfs(node):
            if node == n: 
                return 1 
            
            ans = 0
            
            for nei, _ in neighbours[node]:
                if to_n[node] > to_n[nei]:
                    ans = (ans + dfs(nei)) % MOD
            
            return ans
        
        return dfs(1)
        
        
