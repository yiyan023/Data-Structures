class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # the number of stones we can remove is equal to # of stones - # of connected stones (components)
        # if we have stone with no shared row or column for example, we cannot remove it, so we need to reduce number of stones we can remove by 1 
        # if we have 3 stones that share row/column, then we can max remove 2 

        visited = set()
        rows = defaultdict(set)
        cols = defaultdict(set)
        connections = 0

        for r, c in stones:
            rows[r].add((r, c))
            cols[c].add((r, c))
        
        def dfs(r, c):
            if (r, c) in visited:
                return 
            
            visited.add((r, c))

            for nei_r, nei_c in rows[r]:
                dfs(nei_r, nei_c)
            
            for nei_r, nei_c in cols[c]:
                dfs(nei_r, nei_c)
            
            return
            
        for r, c in stones:
            if (r, c) not in visited:
                dfs(r, c)
                connections += 1
        
        return len(stones) - connections

