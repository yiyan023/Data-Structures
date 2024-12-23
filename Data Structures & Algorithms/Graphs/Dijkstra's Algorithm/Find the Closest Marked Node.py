class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        min_distance = [float('inf')] * n
        neighbours = [[] for _ in range(n)]
        min_heap = [(0, s)]

        for st, e, w in edges:
            neighbours[st].append((e, w))
        
        while min_heap:
            weight, node = heapq.heappop(min_heap)
            min_distance[node] = min(weight, min_distance[node]) 

            for nei, w in neighbours[node]:
                if min_distance[node] + w < min_distance[nei]:
                    heapq.heappush(min_heap, (min_distance[node] + w, nei))
        
        res = min(min_distance[mark] for mark in marked)
        return res if res != float('inf') else -1
    
