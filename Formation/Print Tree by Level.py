from collections import deque 

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value 
        self.left = left 
        self.right = right

def levelOrder(node: TreeNode) -> list[list[int]]:
    if not node:
        return []
    
    res = []
    queue = deque()
    queue.append(node)

    while queue:
        lvl = []

        for _ in range(len(queue)):
            node = queue.popleft()
            lvl.append(node.value)

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        res.append(lvl)
    
    return res

# Single Node Tree
root1 = TreeNode(1)
print(levelOrder(root1) == [[1]])  # Expected Output: [[1]]

# Balanced Binary Tree
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
print(levelOrder(root2) == [[1], [2, 3]])  # Expected Output: [[1], [2, 3]]

# Left-Skewed Tree
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.left.left = TreeNode(3)
print(levelOrder(root3) == [[1], [2], [3]])  # Expected Output: [[1], [2], [3]]
