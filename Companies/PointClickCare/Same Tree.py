class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(r1, r2):
            if not r1 and not r2:
                return True
            
            if not r1 or not r2 or r1.val != r2.val:
                return False 
            
            return dfs(r1.left, r2.left) and dfs(r1.right, r2.right)
        
        return dfs(p, q)
