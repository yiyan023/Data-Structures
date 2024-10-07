# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque()
        queue.append(root)
        cur_level = 1
        max_sum, max_lvl = float('-inf'), 1

        while queue:
            lvl_sum = 0

            for i in range(len(queue)):
                node = queue.popleft()
                lvl_sum += node.val if node else 0
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            if lvl_sum > max_sum:
                max_sum = lvl_sum
                max_lvl = cur_level
            
            cur_level += 1

        return max_lvl
