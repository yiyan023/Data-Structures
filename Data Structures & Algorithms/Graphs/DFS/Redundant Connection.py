class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # removing edge in the cycle
        neighbours = defaultdict(list)

        def dfs(node, prev):
            if node in visited:
                return True
            
            visited.add(node)

            for n in neighbours[node]:
                if n == prev:
                    continue 
                
                if dfs(n, node):
                    return True 
            
            return False
        
        for s, e in edges:
            neighbours[s].append(e)
            neighbours[e].append(s)
            visited = set()

            if dfs(s, -1):
                return [s, e]

        return []
        
        
