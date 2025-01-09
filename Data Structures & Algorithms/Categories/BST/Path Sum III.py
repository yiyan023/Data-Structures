class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = {0:1}

        def dfs(acc, root):
            if not root:
                return 0
            
            acc += root.val
            cur = prefix[acc - targetSum]
            prefix[acc] += 1

            cur += dfs(acc, root.right)
            cur += dfs(acc, root.left)
            prefix[acc] -= 1 # do not want it to account for other paths 

            return cur
        
        return dfs(0, root)
