# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        cur = root
        successor = None

        while cur:
            if p.val >= cur.val:
                cur = cur.right 
            
            else:
                successor = cur
                cur = cur.left 
        
        return successor
