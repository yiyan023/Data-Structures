class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def dfs(i, cur, total):
            # check whether the total is equal to the target
            if target == total:
                result.append(cur.copy())
                return # break out
            
            if i >= len(candidates) or total > target:
                return 

            # include the current element 
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # excluding the element 
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0) # initial condition 
        return result