# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot):    
        if not root:
            return False 
        
        if not subRoot:
            return True 
        
        if self.sameTree(root, subRoot):
            return True 
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, t1, t2):
        if not t1 and not t2:
            return True 
        
        if not t1 or not t2:
            return False
        
        if t1.val != t2.val:
            return False
            
        return self.sameTree(t1.left, t2.left) and self.sameTree(t1.right, t2.right)