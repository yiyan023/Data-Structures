from typing import Optional

class Node:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

def find_closest_value_in_bst(root: Node, target: float) -> int:
    closest_val = float('inf')

    def dfs(root, target):
        nonlocal closest_val

        if not root:
            return 
        
        if abs(root.val - target) < abs(closest_val - target):
            closest_val = root.val 
        
        if root.val < target:
            dfs(root.right, target)
        
        else:
            dfs(root.left, target)
    
    dfs(root, target)
    return closest_val

# Example BST used for most test cases
#               7
#        5              12
#     3     6       9        17
#  1   4         8   10  13    20
root = Node(7)
root.left = Node(5)
root.right = Node(12)
root.left.left = Node(3)
root.left.right = Node(6)
root.right.left = Node(9)
root.right.right = Node(17)
root.left.left.left = Node(1)
root.left.left.right = Node(4)
root.right.left.left = Node(8)
root.right.left.right = Node(10)
root.right.right.left = Node(13)
root.right.right.right = Node(20)

cases = [
    (-1, [1]),
    (5, [5]),
    (7, [7]),
    (19, [20]),
    (18, [17]),
    (14, [13]),
    (11, [10, 12]),  # either value is acceptable
    (2, [1, 3])      # either value is acceptable
]

for tgt, exp in cases:
    res = find_closest_value_in_bst(root, tgt)
    assert res in exp, f'{tgt} -> {res} (expected one of {exp})'

# Tiny tree edge-case
small = Node(2)
small.left = Node(1)
small.right = Node(3)
assert find_closest_value_in_bst(small, 2.7) == 3

print('All Python tests passed!')
