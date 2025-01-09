class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        neighbours = [[] for _ in range(len(vals))]
        max_sum = float('-inf')
        visited = set()

        for s, e in edges:
            heapq.heappush(neighbours[s], (-vals[e], e))
            heapq.heappush(neighbours[e], (-vals[s], s))
        
        def dfs(node):
            nonlocal max_sum
            
            visited.add(node)
            acc, counter = 0, 0
            cur = neighbours[node].copy()

            while counter < k and cur:
                val, nei = heapq.heappop(cur)
                
                if acc - val <= acc:
                    break
                
                acc -= val
                counter += 1

            max_sum = max(max_sum, acc + vals[node])

            for val, nei in neighbours[node]:
                if nei not in visited:
                    dfs(nei)
        
        for i in range(len(vals)):
            if i not in visited:
                dfs(i)
        
        return max_sum
