class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        outline = [[] for x in range(numCourses)]
        state = [0] * numCourses
        result = []

        for c, p in prerequisites:
            outline[c].append(p)

        def dfs(c):
            if state[c] == 1:
                return False 
            
            if state[c] == 2:
                return True 
            
            state[c] = 1 # officially taking the course!

            for p in outline[c]:
                if not dfs(p):
                    return False 
            
            state[c] = 2 # officially completed! 
            result.append(c)
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return []
        
        return result