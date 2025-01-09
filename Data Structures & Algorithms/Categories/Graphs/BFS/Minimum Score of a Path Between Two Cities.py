class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # the minimum possible score is just equal to the minumum PATH score that is connected to 1
        # this can be done easily with dfs/bfs using the neighbours for 1 (and of its neighbours' neighbours, etc.)
        # we will return a minimum cost, which is just equal to the cost of the path for every city
        # use a visited set to make sure we are not checking cities multiple times

        neighbours = [[] for _ in range(n + 1)]
        queue = collections.deque()
        min_cost = float('inf')
        queue.append(1)
        visited = set()

        for s, e, cost in roads:
            neighbours[s].append((e, cost))
            neighbours[e].append((s, cost))
        
        while queue:
            city = queue.popleft()

            if city in visited:
                continue 
            
            visited.add(city)

            for nei, nei_c in neighbours[city]:
                min_cost = min(min_cost, nei_c)
                queue.append(nei)
        
        return min_cost
