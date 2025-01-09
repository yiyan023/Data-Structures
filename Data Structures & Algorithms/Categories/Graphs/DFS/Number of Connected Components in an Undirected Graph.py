class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        connections = defaultdict(list)
        res = 0

        for s, e in edges:
            connections[s].append(e)
            connections[e].append(s)
        
        def dfs(node):
            visited.add(node)

            for neighbour in connections[node]:
                if neighbour not in visited:
                    dfs(neighbour)
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
        
        return res
