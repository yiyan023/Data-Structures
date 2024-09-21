class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            
            left, right = height(root.right), height(root.left)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)
        
        return height(root) != -1
