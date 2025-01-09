"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node):
        oldNew = {} #

        def dfs(node):
            if node in oldNew:
                return oldNew[node] #if it is in the hash, that means it has already been cloned
            
            copy = Node(node.val) #make a new node
            oldNew[node] = copy #place it inside the hash

            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh)) #dfs(neigh) lets us go through every neighbour & append it to the neighbour on the copy node
            return copy #the return the copy when you are finished
        
        if node:
            return dfs(node) 
        
        return None
