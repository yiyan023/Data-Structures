class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = { (s, e) for s, e in connections} # hash is necessary because it makes it slower for retrieval -> keeps it at O(1)
        neighbours = { i:[] for i in range(n)}
        visit = set()
        result = [0]

        for s, e in connections:
            neighbours[s].append(e)
            neighbours[e].append(s)
        
        def dfs(c):
            for i in neighbours[c]:
                if i in visit:
                    continue 
                
                if (i, c) not in edges: # since we are starting off with zero, this means it is not connected to zero!
                    result[0] += 1
                visit.add(i)
                dfs(i)
        
        visit.add(0)
        dfs(0)
        return result[0]
