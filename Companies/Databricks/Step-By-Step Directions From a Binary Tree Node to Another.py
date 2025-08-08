# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find_lca(root):
            if not root:
                return None
            
            if root.val == startValue or root.val == destValue:
                return root

            left, right = find_lca(root.left), find_lca(root.right)

            if left and right:
                return root 
            
            return left or right
            
        def find_path(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True

            path.append('L')
            if find_path(node.left, target, path):
                return True
            path.pop()

            path.append('R')
            if find_path(node.right, target, path):
                return True
            path.pop()

            return False

        lca = find_lca(root)

        path_to_start = []
        path_to_dest = []

        find_path(lca, startValue, path_to_start)
        find_path(lca, destValue, path_to_dest)

        return 'U' * len(path_to_start) + ''.join(path_to_dest)
