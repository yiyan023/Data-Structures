# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        def checkBST(root, minVal, maxVal):            
            if not root:
                return True 
            
            if root.val >= maxVal or root.val <= minVal:
                return False
            
            return (checkBST(root.left, minVal, root.val) and checkBST(root.right, root.val, maxVal))
        
        return checkBST(root, float('-inf'), float('inf'))