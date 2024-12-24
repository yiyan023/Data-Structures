class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        def dfs(node):
            min_heap = [(0, node)]
            res = [float('inf')] * len(edges)

            while min_heap:
                weight, cur = heapq.heappop(min_heap)
                res[cur] = min(res[cur], weight)

                if 1 + res[cur] < res[edges[cur]] and edges[cur] != -1:
                    heapq.heappush(min_heap, (1 + res[cur], edges[cur]))
            
            return res
        
        min_one = dfs(node1)
        min_two = dfs(node2)

        min_node = 0
        min_path = float('inf')
        impossible = 0

        for i in range(len(min_two)):
            if min_one[i] == float('inf') or min_two[i] == float('inf'):
                impossible += 1
            
            if max(min_one[i], min_two[i]) < min_path:
                min_path = max(min_one[i], min_two[i])
                min_node = i
        
        return min_node if impossible != len(min_one) else -1
