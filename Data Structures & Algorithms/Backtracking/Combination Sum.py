class Solution:
    def combinationSum(self, candidates, target):
        # backtracking problem for sure 
        result = []
        
        def dfs(i, sum, cur):
            if sum > target or i >= len(candidates):
                return 
            
            elif sum == target:
                result.append(cur[:])
                return
            
            cur.append(candidates[i]) # include the current element 
            dfs(i, sum + candidates[i], cur)
            
            cur.pop()
            dfs(i + 1, sum, cur)
        
        dfs(0, 0, [])
        return result
            