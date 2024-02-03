class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        neighbour = [[] for x in range(numCourses)] #initialize the neighbour 
        indegree = [0] * numCourses #initialize indegree 

        for pre in prerequisites:
            #append the courses [0] to the prereq [1]
            neighbour[pre[1]].append(pre[0])
            indegree[pre[0]] += 1 #indicates # of prereqs

        queue = [] #implement a queue

        for i in range(len(indegree)):
            if indegree[i] == 0: #the index is important because it represents the course!
                queue.append(i) #starting at the edge -- the first prereqs

        visited = 0 #visited pointer

        while queue: 
            course = queue.pop(0)
            visited += 1
            for neigh in neighbour[course]: 
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        
        print(indegree)
        return numCourses == visited

        

        