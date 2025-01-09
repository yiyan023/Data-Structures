class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = set()
        visited = set()

        def dfs(node):
            if node in res:
                return True
            
            if node in visited:
                return False 
            
            visited.add(node)
            
            for nei in graph[node]:
                if not dfs(nei):
                    return False

            res.add(node)
            return True
        
        for i in range(len(graph)):
            dfs(i)
        
        return sorted(res)
