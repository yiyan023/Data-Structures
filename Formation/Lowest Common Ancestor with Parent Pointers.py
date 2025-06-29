class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    
def lowest_common_ancestor(p, q):
    # the trick for this problem is that you are given the two nodes and we want to work backwards 

    # go through all the possible parents of p & mark them as visited 

    # go backwards in q
    # if you run into a parent that has already been visited, return that value 

    seen = set()

    while p:
        seen.add(p.value)
        p = p.parent
    
    while q:
        if q.value in seen:
            return q
        
        q = q.parent 
    
