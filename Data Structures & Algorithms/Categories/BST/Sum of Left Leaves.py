class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root, isLeft):
            if not root: return 0
            if not root.left and not root.right and isLeft: return root.val 
            return dfs(root.right, False) + dfs(root.left, True)
        
        return dfs(root, False)
