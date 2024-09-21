class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(r1, r2):
            if not r1 and not r2:
                return True 
            
            if not r1 or not r2 or r1.val != r2.val:
                return False
            
            return sameTree(r1.right, r2.right) and sameTree(r1.left, r2.left) 

        def dfs(root):
            if not root:
                return False 
            
            if sameTree(root, subRoot):
                return True
            
            return dfs(root.right) or dfs(root.left)
        
        return dfs(root)
