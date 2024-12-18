class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbours = defaultdict(list)
        visited = set()

        if not len(edges):
            return True

        for s, e in edges: # undirected graph
            neighbours[s].append(e)
            neighbours[e].append(s)
        
        def dfs(s, e):
            visited.add(s)
            
            for n in neighbours[s]:
                if n == e:
                    return True 
                
                if n not in visited and dfs(n, e):
                    visited.add(n)
                    return True 
            
            return False 

        return dfs(source, destination)
