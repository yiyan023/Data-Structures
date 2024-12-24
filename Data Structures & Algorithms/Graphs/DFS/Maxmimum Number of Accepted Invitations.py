class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        matches = [-1] * len(grid[0]) # number of invitations accepted by girls

        def dfs(boy):
            for girl in range(len(grid[0])):
                if girl not in visited and grid[boy][girl]:
                    visited.add(girl)

                    if matches[girl] == -1 or dfs(matches[girl]):
                        matches[girl] = boy 
                        return True 
            
            return False
        
        invitations = 0

        for boy in range(len(grid)):
            visited = set()

            if dfs(boy):
                invitations += 1
        
        return invitations
            
