class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        neighbours = defaultdict(list)
        max_heap = [(-1, start_node)]
        max_prob = [0] * n
        max_prob[start_node] = 1
        
        for i, (s, e) in enumerate(edges):
            neighbours[s].append((e, succProb[i]))
            neighbours[e].append((s, succProb[i]))
        
        while max_heap:
            prob, node = heapq.heappop(max_heap)
            prob = -prob

            if node == end_node:
                return prob
        
            for nei, p in neighbours[node]:
                new_prob = p * prob
                
                if new_prob > max_prob[nei]:
                    max_prob[nei] = new_prob
                    heapq.heappush(max_heap, (-new_prob, nei))
        
        return 0
