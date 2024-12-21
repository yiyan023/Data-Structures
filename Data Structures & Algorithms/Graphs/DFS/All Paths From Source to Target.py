class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        
        def dfs(node, path):
            path.append(node)

            if node == len(graph) - 1:
                res.append(path.copy())
            
            else:
                for nei in graph[node]:
                    dfs(nei, path)
            
            path.pop()

        dfs(0, [])  # Start DFS from the source node (0)
        return res
