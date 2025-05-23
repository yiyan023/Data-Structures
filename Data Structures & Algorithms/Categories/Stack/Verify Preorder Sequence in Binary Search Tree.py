class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # root -> left -> right 

        # everything less than the root appears before everything greater than the root

        # stack?

        stack = []
        max_root = 0

        for num in preorder:
            while stack and stack[-1] < num:
                max_root = max(max_root, stack.pop())
            
            if num < max_root:
                return False 
            
            stack.append(num)
        
        return True
