# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        # dfs returns a tuple:
        # (dist_node_to_nearest_leaf, has_k_in_subtree, dist_k_to_this_node, chosen_leaf_val)
        graph = collections.defaultdict(list)
        outgoing = collections.defaultdict(int)

        def dfs(node, par = None):
            if node:
                if par:
                    graph[node.val].append(par.val)
                    graph[par.val].append(node.val)
                    outgoing[par.val] += 1
                
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        queue = deque()
        queue.append(k)
        seen = set()
        seen.add(k)
        
        while queue:
            node = queue.popleft()

            if not outgoing[node]:
                return node

            for neigh in graph[node]:
                if not outgoing[neigh]:
                    return neigh 
                
                if neigh not in seen:
                    queue.append(neigh)
                    seen.add(neigh)
        
        return root.val
