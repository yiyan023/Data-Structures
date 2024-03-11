class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
        
class Solution:
    def copyRandomList(self, head):
        copy = {None: None} # initialize the hash so you can map nodes to nodes

        # first passing: initialize each node
        cur = head 
        while cur:
            copy[cur] = Node(cur.val)
            cur = cur.next
        
        # second passing: indicate next & random pointers for each node
        cur = head 
        while cur:
            newNode = copy[cur]
            newNode.next = copy[cur.next]
            newNode.random = copy[cur.random]
            cur = cur.next
        
        return copy[head]

        