# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        from collections import deque 
        queue = deque() #set up queue

        queue.append(root) #append the root to the queue (initial)
        result = [] #what you will return
        
        while queue:
            lvl = []
            qLen = len(queue) #make sure to reset the length everytime 
            for i in range(qLen):
                node = queue.popleft()

                if node: #if its empty then dont do this
                    lvl.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if lvl:
                result.append(lvl) #if level array is not empty
        return result 