class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        neighbours = defaultdict(list)

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                s1, e1 = points[i]
                s2, e2 = points[j]
                dist = abs(s1 - s2) + abs(e1 - e2)

                neighbours[i].append((dist, j))
                neighbours[j].append((dist, i))
        
        # prim's algorithm 
        res = 0
        visited = set()
        min_heap = [[0, 0]]

        while len(visited) < len(points):
            dist, node = heapq.heappop(min_heap)

            if node in visited:
                continue 
            
            visited.add(node)
            res += dist
            
            for nei_dist, nei in neighbours[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (nei_dist, nei))
        
        return res

                

