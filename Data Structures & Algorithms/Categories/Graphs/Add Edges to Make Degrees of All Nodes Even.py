class Solution:
    def __init__(self):
        self.neighbours = defaultdict(set)
        self.odd_nodes = set()
        self.n = 0

    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        self.n = n

        for s, e in edges:
            self.odd_nodes.add(s) if s not in self.odd_nodes else self.odd_nodes.remove(s)
            self.odd_nodes.add(e) if e not in self.odd_nodes else self.odd_nodes.remove(e)
            
            self.neighbours[s].add(e)
            self.neighbours[e].add(s)
        
        if len(self.odd_nodes) % 2 or len(self.odd_nodes) > 4:
            return False
        
        return self.check_neighbours(len(self.odd_nodes), list(self.odd_nodes))
        
    def is_neighbours(self, s, e):
        return s in self.neighbours[e]
        
    def check_combinations(self, a, b, c, d):
        comb1 = not self.is_neighbours(a, b) and not self.is_neighbours(c, d)
        comb2 = not self.is_neighbours(a, c) and not self.is_neighbours(b, d)
        comb3 = not self.is_neighbours(a, d) and not self.is_neighbours(b, c)

        return comb1 or comb2 or comb3
        
    def check_even_nodes(self, a, b):
        for node in range(1, self.n + 1):
            if node == a or node == b:
                continue 
            
            if not self.is_neighbours(a, node) and not self.is_neighbours(b, node):
                return True 
        
        return False
        
    def check_neighbours(self, length, arr):
        match length:
            case 0:
                return True
            
            case 2:
                if not self.is_neighbours(arr[0], arr[1]):
                    return True
                return self.check_even_nodes(arr[0], arr[1])
            
            case 4:
                return self.check_combinations(arr[0], arr[1], arr[2], arr[3])
            
            case _:
                raise ValueError(f"Unsupported length: {length}")
