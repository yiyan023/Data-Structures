class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        neighbours = [[x+1] for x in range(n-1)]
        res = []
        
        def find_dist():
            dp = [float('inf')] * n
            dp[n-1] = 0 # base case 

            for i in range(n-2, -1, -1):
                for nei in neighbours[i]:
                    dp[i] = min(dp[i], 1 + dp[nei])
            
            return dp[0]
        
        for s, e in queries:
            neighbours[s].append(e)
            cur = find_dist()
            res.append(cur)
        
        return res
