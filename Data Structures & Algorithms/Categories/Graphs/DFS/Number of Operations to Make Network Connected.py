class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        neighbours = [[] for _ in range(n)]
        visit = set()
        groups = 0

        # set up neighbours adjacent array 
        for s, e  in connections:
            neighbours[s].append(e)
            neighbours[e].append(s)
        
        def dfs(comp):
            if comp in visit:
                return 
            
            visit.add(comp)

            for nei in neighbours[comp]:
                dfs(nei)
        
        for comp in range(n):
            if comp not in visit:
                dfs(comp)
                groups += 1
        
        return groups - 1
