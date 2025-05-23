class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque([root])
        backwards = False
        res = []

        while queue:
            lvl = []

            for _ in range(len(queue)):
                node = queue.popleft()

                if node:
                    lvl.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if lvl:
                if backwards:
                    lvl.reverse()
                    
                res.append(lvl)
            
            backwards = not backwards
        
        return res
