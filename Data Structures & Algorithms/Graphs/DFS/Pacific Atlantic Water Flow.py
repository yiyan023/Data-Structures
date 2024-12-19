class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[1, 0], [0,1], [-1, 0], [0,-1]]
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, ocean):
            ocean.add((r, c))
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if (0 <= new_r < len(heights) and 0 <= new_c < len(heights[0]) and
                    (new_r, new_c) not in ocean and heights[new_r][new_c] >= heights[r][c]):
                    dfs(new_r, new_c, ocean)

        for r in range(len(heights)):
            dfs(r, 0, pacific)
            dfs(r, len(heights[0])-1, atlantic)  

        for c in range(len(heights[0])):
            dfs(0, c, pacific)
            dfs(len(heights)-1, c, atlantic)
                
        
        res = list(pacific & atlantic)
        return res

            
