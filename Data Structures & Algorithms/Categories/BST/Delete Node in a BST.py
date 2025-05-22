# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def successor(root):
            res = root.right

            while res and res.left:
                res = res.left
            
            return res.val 
        
        def precessor(root):
            res = root.left

            while res and res.right:
                res = res.right 
            
            return res.val
        
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            
        elif root.val < key:
            root.right = self.deleteNode(root.right, key) 
            
        else:
            if not root.left and not root.right:
                return None 
            
            if root.right:
                root.val = successor(root) # to keep bst, find smallest value in right subtree
                root.right = self.deleteNode(root.right, root.val)
            
            else:
                root.val = precessor(root)
                root.left = self.deleteNode(root.left, root.val)
            
        return root
