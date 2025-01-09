class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        precourses = defaultdict(int)
        nextcourses = [[] for _ in range(n + 1)]
        visit = set()
        sems = 0

        for prev, nxt in relations:
            precourses[nxt] += 1
            nextcourses[prev].append(nxt)
        
        queue = collections.deque()

        for i in range(1, n+1):
            if not precourses[i]:
                queue.append(i)
        
        while queue:
            for i in range(len(queue)):
                course = queue.popleft()

                if not precourses[course]:
                    visit.add(course)

                for prereq in nextcourses[course]:
                    precourses[prereq] -= 1

                    if not precourses[prereq]:
                        queue.append(prereq)
            
            sems += 1
        
        return sems if len(visit) == n else -1
    
        
            
