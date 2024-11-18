class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkValidity(root, min_val, max_val):
            if not root:
                return True 
            
            return min_val < root.val < max_val and checkValidity(root.left, min_val, root.val) and checkValidity(root.right, root.val, max_val)
        
        return checkValidity(root, float('-inf'), float('inf'))
