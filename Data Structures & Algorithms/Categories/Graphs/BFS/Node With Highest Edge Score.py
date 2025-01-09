class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        res = [0] * len(edges)
        max_score = 0
        node = 0

        for i, nei in enumerate(edges):
            res[edges[i]] += i
        
        for i, score in enumerate(res):
            if score > max_score:
                node = i
                max_score = max(score, max_score)
        
        return node
