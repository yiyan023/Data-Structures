class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:
            lvl = []

            for i in range(len(queue)):
                cur = queue.popleft()

                if cur:
                    lvl.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
            
            res.append(lvl[-1]) if lvl else None
        
        return res
