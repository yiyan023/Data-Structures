class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # detecting cycles 

        neighbours = defaultdict(list)
        visited = set()

        for s, e in edges:
            neighbours[s].append(e)
            neighbours[e].append(s)
        
        def dfs(node, prev):
            visited.add(node)

            for n in neighbours[node]:
                if n == prev:
                    continue 
                
                if n in visited:
                    return True 
                
                elif dfs(n, node):
                    return True
            
            return False
        
        if dfs(0, -1):
            return False
        
        return len(visited) == n
