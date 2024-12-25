# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        max_avg = 0
        
        def dfs(root):
            nonlocal max_avg
            if not root:
                return (0, 0)

            left, right = dfs(root.left), dfs(root.right)
            
            acc = left[0] + right[0] + root.val
            nodes = 1 + left[1] + right[1]
            max_avg = max(max_avg, acc / nodes)

            return (acc, nodes)
        
        dfs(root)
        return max_avg



