class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        neighbours = defaultdict(list)
        max_paths = [0] * len(cost)
        seen = set()

        for s, e in edges:
            neighbours[s].append(e)
            neighbours[e].append(s)
        
        def dfs(node, acc):
            if node and len(neighbours[node]) == 1:
                max_paths[node] = max(max_paths[node], cost[node])
                return cost[node]
            
            seen.add(node)

            for child in neighbours[node]:
                if child not in seen:
                    seen.add(child)

                    child_path = dfs(child, acc + cost[node])
                    max_paths[node] = max(max_paths[node], cost[node] + child_path)
            
            return max_paths[node]
        
        dfs(0, 0)
        seen = set()
        res = 0
        
        def count_changes(node, acc):
            nonlocal res
            if acc + max_paths[node] != max_paths[0]:
                acc += (max_paths[0] - acc - max_paths[node])
                res += 1
            
            seen.add(node)
            
            for child in neighbours[node]:
                if child not in seen:
                    seen.add(child)
                    count_changes(child, acc + cost[node])

            return 
        
        count_changes(0, 0)
        return res

                
        



            
