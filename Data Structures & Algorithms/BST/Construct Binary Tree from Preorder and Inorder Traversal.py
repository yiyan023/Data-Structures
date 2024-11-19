# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        
        res = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])

        res.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        res.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return res

