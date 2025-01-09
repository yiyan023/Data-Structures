class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, arr, acc):
            if acc == target:
                res.append(arr)
                return 
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j-1] == candidates[j]:
                    continue
                
                if acc + candidates[j] > target:
                    break
                
                dfs(j+1, arr + [candidates[j]], acc + candidates[j])
        
        candidates.sort()
        dfs(0, [], 0)
        return res
                
