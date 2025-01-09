class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def bfs(root):
            if not root:
                return 0
            
            return 1 + bfs(root.left) + bfs(root.right)
        
        return bfs(root)
