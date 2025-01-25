class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # hash -> incoming edges for each node
        # flip the array direction for dfs 

        visited = set()
        dp = [False] * len(graph)
        res = []

        def dfs(node):
            if not graph[node]:
                dp[node] = True 
                return True
            
            if dp[node]:
                return True
            
            elif node in visited:
                return False 
            
            visited.add(node)

            for nei in graph[node]:
                if not dfs(nei):
                    return False 
            
            dp[node] = True
            return True 
        
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)

        return res
