class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left         
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, p, q):
        if not p and not q:
            return True 
        
        if not q or not p:
            return False 
        
        if q.val != p.val:
            return False 
        
        return self.isMirror(p.right, q.left) and self.isMirror(p.left, q.right)