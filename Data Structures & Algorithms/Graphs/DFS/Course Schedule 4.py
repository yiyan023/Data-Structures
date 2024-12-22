class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        visit = [False] * numCourses
        prereqs = [set() for _ in range(numCourses)]
        res = []

        def dfs(course):
            if visit[course]: 
                return prereqs[course]
            
            visit[course] = True 

            for prev in list(prereqs[course]):
                prereqs[course].update(dfs(prev))
            
            return prereqs[course]

        for start, end in prerequisites:
            prereqs[end].add(start)

        for course in range(numCourses):
            dfs(course)

        for pre, nxt in queries:
            res.append(pre in prereqs[nxt])
        
        return res
