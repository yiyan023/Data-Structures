def immediateParentSum(root: Node) -> Node:
    
    def explore(node: Node, parentVal: int):
        if not node:
            return 
        
        explore(node.left, node.val)
        explore(node.right, node.val)

        node.val += parentVal 
    
    explore(root, 0)
    return root 
    
print(immediateParentSum(None) == None)
