class Solution(object):
    def widthOfBinaryTree(self, root):
        result = 0
        q = collections.deque()
        q.append((root, 1))

        while q:
            row = []

            for i in range(len(q)):
                node, val = q.popleft()
                row.append(val)
                if node.left: q.append((node.left, val * 2))
                if node.right: q.append((node.right, val * 2 + 1))
            
            result = max(result, row[-1] - row[0] + 1)
        
        return result
