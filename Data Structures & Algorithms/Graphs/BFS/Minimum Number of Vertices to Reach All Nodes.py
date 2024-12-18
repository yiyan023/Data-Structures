class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # must be all outgoing edges because we cannot reach them

        has_incoming_edges = [False for _ in range(n)]

        for s, e in edges:
            has_incoming_edges[e] = True 
        
        res = [node for node in range(n) if not has_incoming_edges[node]]
        return res
