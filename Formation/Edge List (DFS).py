from collections import defaultdict

def sumNodes(vertexList: list, edgeList: list, startNode: int):
    if startNode not in vertexList:
        return 0
    
    neighbours = defaultdict(list)
    seen = set()

    for s, e in edgeList:
        neighbours[s].append(e)
        neighbours[e].append(s)

    def dfs(node):
        if node in seen:
            return 0
        
        res = node 
        seen.add(node)

        for neigh in neighbours[node]:
            if neigh not in seen:
                res += dfs(neigh)
                seen.add(neigh)
        
        return res
    
    return dfs(startNode)

vertexList = [1, 2, 3, 4, 5]
edgeList = [(1, 2), (2, 3), (1, 3)]

print(sumNodes(vertexList, edgeList, 1))
print(sumNodes(vertexList, edgeList, 10000))
print(sumNodes(vertexList, edgeList, 4))
