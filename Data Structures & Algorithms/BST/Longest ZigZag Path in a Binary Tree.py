# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxLen = 0

        def left(node, len):
            if not node:
                return len
            
            return max(right(node.left, len + 1), left(node.right, 1))

        def right(node, len):
            if not node:
                return len

            return max(left(node.right, len + 1), right(node.left, 1))

        maxLen = max(maxLen, left(root, 0), right(root, 0))
        return maxLen-1

