class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbours = defaultdict(list)
        
        for s, e in edges:
            neighbours[s].append(e)
        
        visited = set()
        memo = {}
        
        def dfs(node):
            if node in memo:
                return memo[node]
            
            if node in visited:
                return False
            
            if not neighbours[node]:
                return node == destination
 
            visited.add(node)
            
            for nei in neighbours[node]:
                if not dfs(nei):
                    return False
            
            memo[node] = True
            return True
        
        # Start DFS from the source
        return dfs(source)
