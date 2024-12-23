class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        suspicious = set()
        visited = set()
        neighbours = [[] for _ in range(n)]
        nodes = [x for x in range(n)]

        for s, e in invocations:
            neighbours[s].append(e)
        
        def dfs(node):
            if node in visited:
                return 
            
            visited.add(node)
            suspicious.add(node)

            for nei in neighbours[node]:
                if nei not in visited:
                    dfs(nei)
        
        dfs(k)

        for node in range(n):
            if node not in suspicious:
                for nei in neighbours[node]:
                    if nei in suspicious:
                        return nodes

        return [x for x in nodes if x not in suspicious]

