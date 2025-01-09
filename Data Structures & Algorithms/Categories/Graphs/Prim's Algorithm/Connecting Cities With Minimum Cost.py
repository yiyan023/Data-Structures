class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # this is also prim's algorithm, where we want to find the minimum spanning tree

        min_heap = [(0, 1)]
        neighbours = [[] for _ in range(n+1)]
        visited = set()
        res = 0

        for s, e, w in connections:
            neighbours[e].append((s, w))
            neighbours[s].append((e, w))
        
        while min_heap:
            cost, node = heapq.heappop(min_heap)

            if node not in visited:
                visited.add(node) # we already found the shortest distance to this node
                res += cost # add the shortest value to result

                for nei, weight in neighbours[node]:
                    heapq.heappush(min_heap, (weight, nei))
        
        return res if len(visited) == n else -1
