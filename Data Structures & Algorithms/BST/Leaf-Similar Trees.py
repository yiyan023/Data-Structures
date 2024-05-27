# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  
class Solution(object):
    def leafSimilar(self, root1, root2):
        def findleaf(root):
            left, right = [], []
            # do not have to consider the case where it is non-empty
            if not root.right and not root.left:
                return [root.val] #  base case: return an array of just itself 
            else:
                if root.right:
                    right = findleaf(root.right) # traverse right 
                if root.left:
                    left = findleaf(root.left) # traverse keft
                return left + right 

        
        one, two = findleaf(root1), findleaf(root2)
        print(one, two)
        return one == two # use arrays bc order matters!
        
