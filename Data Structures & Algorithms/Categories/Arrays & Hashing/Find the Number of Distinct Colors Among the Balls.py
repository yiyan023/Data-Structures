class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        colors = defaultdict(int)
        res = []

        for ball, color in queries:
            if ball in balls:
                colors[balls[ball]] -= 1

                if colors[balls[ball]] == 0:
                    colors.pop(balls[ball])
            
            balls[ball] = color
            colors[color] += 1
            res.append(len(colors))
        
        return res
