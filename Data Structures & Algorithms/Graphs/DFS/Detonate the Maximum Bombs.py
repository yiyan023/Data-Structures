class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        neighbours = defaultdict(list)
        res = 0
        
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                b1, b2 = bombs[i], bombs[j]

                dist = (b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2
                if b1[2] ** 2  >= dist:
                    neighbours[i].append(j)
                
                if b2[2] ** 2 >= dist:
                    neighbours[j].append(i)
        
        def dfs(bomb):
            if bomb in visited:
                return 0
            
            visited.add(bomb)
            res = 0

            for nei in neighbours[bomb]:
                if nei not in visited:
                    res += 1 + dfs(nei)
            
            return res

        for i in range(len(bombs)):
            visited = set()
            detonations = dfs(i)
            res = max(res, detonations)
        
        return res + 1
