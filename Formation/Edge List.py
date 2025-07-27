from collections import defaultdict, deque

def sumNodes(vertexList: list, edgeList: list, startNode: int) -> int:
    neighbours = defaultdict(list)
    res = 0

    for s, e in edgeList:
        neighbours[s].append(e)
        neighbours[e].append(s)
    
    if startNode not in set(vertexList):
        return 0
    
    seen = set()
    seen.add(startNode)

    queue = deque()
    queue.append(startNode)
    

    while queue:
        node = queue.popleft()
        res += node

        for neighbour in neighbours[node]:
            if neighbour not in seen:
                seen.add(neighbour)
                queue.append(neighbour)
    
    return res

vertexList = [1, 2, 3, 4, 5]
edgeList = [(1, 2), (2, 3), (1, 3)]
print(sumNodes(vertexList, edgeList, 1))

vertexList: [1, 2, 3, 4, 5]
edgeList: [(2, 1), (3, 2), (3, 1)]

print(sumNodes(vertexList, edgeList, 1))
print(sumNodes(vertexList, edgeList, 10000))
print(sumNodes(vertexList, edgeList, 4))
