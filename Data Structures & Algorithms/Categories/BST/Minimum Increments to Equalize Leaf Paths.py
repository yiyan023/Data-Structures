class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        neighbours = defaultdict(list)
        seen = set()
        res = 0

        for s, e in edges:
            neighbours[s].append(e)
            neighbours[e].append(s)
        
        test = []
        
        def dfs(node, acc):
            nonlocal res
            if node and len(neighbours[node]) == 1:
                return cost[node]
            
            seen.add(node)
            child_paths = []

            for child in neighbours[node]:
                if child not in seen:
                    seen.add(child)

                    child_path = dfs(child, acc + cost[node])
                    child_paths.append(child_path)
            
            max_path = max(child_paths)

            for child_path in child_paths:
                if child_path != max_path:
                    res += 1

            return max_path + cost[node]
        
        dfs(0, 0)
        return res
