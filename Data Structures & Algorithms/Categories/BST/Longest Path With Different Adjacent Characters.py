
class Node:
    def __init__(self, val: int, children_num: int):
        self.val = val 
        self.children = [None] * children_num

class Solution:
    def longestPath(self, parent: list[int], s: str) -> int:
        neighbours = defaultdict(list)
        max_path = 0

        for node, parent_node in enumerate(parent):
            neighbours[parent_node].append((node, s[node]))

        def dfs(root, val):
            nonlocal max_path

            if not neighbours[root]:
                max_path = max(max_path, 1)
                return 1
            
            longest_path, second_longest_path = 0, 0

            for child, child_val in neighbours[root]:
                path = dfs(child, child_val)

                if val != child_val:
                    if path > longest_path:
                        second_longest_path = longest_path
                        longest_path = path
                    
                    elif path > second_longest_path:
                        second_longest_path = path
            
            max_path = max(max_path, 1 + longest_path + second_longest_path)
            return 1 + longest_path 
            
        dfs(0, s[0])
        return max_path
