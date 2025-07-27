class Node:
    def __init__(self, value: int, children = []):
        self.value = value 
        self.children = children
    
def hasPathTo(node: Node, target: int) -> bool:
    seen = set()
    
    def dfs(root, target):
        if not root or root in seen:
            return False 
        
        seen.add(root)
        
        if root.value == target:
            return True 

        for child in root.children:
            if child not in seen:
                if dfs(child, target):
                    return True
        
        return False

    return dfs(node, target)

node = Node(1, [Node(2), Node(3)])

# standalone version
print(hasPathTo(node, 3) == True)
print(hasPathTo(node, 4) == False)

node = Node(12, [
  Node(18, [Node(1), Node(4, [Node(3), Node(9)])])
])

  # standalone version
print(hasPathTo(node, 9) == True)
print(hasPathTo(node, 14) == False)
print(hasPathTo(node, 0) == False)
print(hasPathTo(None, 0) == False)
print(hasPathTo(node, 12) == True)

node = Node(1)

# standalone version
print(hasPathTo(node, 1) == True)
print(hasPathTo(node, 2) == False)

node = Node(1, [Node(2), Node(3)])
cycleNode = Node(5, [node])
node.children.append(cycleNode)

# standalone version
print(hasPathTo(node, 1) == True)
print(hasPathTo(node, 2) == True)
print(hasPathTo(node, 5) == True)
print(hasPathTo(node, 4) == False)

node = Node(12, [
  Node(18, [Node(5), Node(5, [Node(5), Node(5)])])
])

# standalone version
print(hasPathTo(node, 12) == True)
print(hasPathTo(node, 5) == True)
print(hasPathTo(node, 4) == False)

cycleNode1 = Node(3)
cycleNode2 = Node(2)
cycleNode1.children.append(cycleNode2)
cycleNode2.children.append(cycleNode1)
node = Node(12, [
  Node(18, [Node(5), cycleNode1, Node(5, [
    Node(5), cycleNode2, Node(5)])])])

# standalone version
print(hasPathTo(node, 12) == True)
print(hasPathTo(node, 2) == True)
print(hasPathTo(node, 3) == True)
print(hasPathTo(node, 5) == True)
print(hasPathTo(node, 4) == False)
