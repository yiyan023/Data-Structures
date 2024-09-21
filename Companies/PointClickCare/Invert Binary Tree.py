class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def bfs(root):
            if not root:
                return 
            
            temp = root.right 
            root.right = root.left 
            root.left = temp
            
            bfs(root.left)
            bfs(root.right)
        
        bfs(root)
        return root
