# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def goodNodes(self, root):
        def dfs(root, prev):

            if not root:
                return 0
            
            if root.val >= prev:
                left, right = dfs(root.left, root.val), dfs(root.right, root.val)
                return 1 + left + right
            else: 
                left, right = dfs(root.left, prev), dfs(root.right, prev) #new root value is not the max
                return left + right
            
        return dfs(root, root.val) #root.val is the initial maximum value!
        