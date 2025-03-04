"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # inorder traversal, storing nodes in a queue 

        queue = deque()
        queue.append(root)

        while queue:
            lvl = []

            for i in range(len(queue)):
                node = queue.popleft()

                if node: 
                    lvl.append(node)
                    queue.append(node.left)
                    queue.append(node.right)
        

            for i, cur in enumerate(lvl):
                if i + 1 < len(lvl):
                    cur.next = lvl[i+1]
        
        return root

            
