# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:   
            max_node = float('-inf')

            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node:
                    max_node = max(max_node, node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            
            res.append(max_node)   
        
        return res[:-1]
