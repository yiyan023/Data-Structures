class TrieNode:
    def __init__(self):
        self.end_word = False
        self.left = None 
        self.right = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, bin):
        cur = self.root
        
        for c in bin:
            if c == "0":
                if not cur.left:
                    cur.left = TrieNode()
                cur = cur.left
            
            else:
                if not cur.right:
                    cur.right = TrieNode()
                cur = cur.right
        
        cur.end_word = True
    
class maxDistance:    
    def findDistance(self, arr):
        trie = Trie()
        maxDistance = 0
        
        for s in arr:
            trie.insert(s)
        
        def calculateDiameter(trie):
            nonlocal maxDistance
            if not trie:
                return 0

            left, right = calculateDiameter(trie.left), calculateDiameter(trie.right)
            if left and right:
                maxDistance = max(maxDistance, left+right)

            return 1 + max(left, right)
        
        calculateDiameter(trie.root)
        return maxDistance

if __name__ == "__main__":
    arr = ["1011000", "1011110"]
    md = maxDistance()
    max_dist = md.findDistance(arr)
    print(max_dist)
    
        
        
