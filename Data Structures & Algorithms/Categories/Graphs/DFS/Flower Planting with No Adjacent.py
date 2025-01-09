class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        neighbours =[[] for _ in range(n + 1)]
        not_type = [set() for _ in range(n + 1)]
        res = [0] * (n + 1)

        for s, e in paths:
            neighbours[s].append(e)
            neighbours[e].append(s)
        
        def dfs(node):
            for num in range(1, 5):
                if num not in not_type[node]:
                    res[node] = num

                    for nei in neighbours[node]:
                        if not res[nei]:
                            not_type[nei].add(num)
                    
                    for nei in neighbours[node]:
                        if not res[nei]:
                            dfs(nei)
                
                    break
        
        for i in range(1, n + 1):
            dfs(i)
    
        return res[1:]
        
