class TrieNode:
    def __init__(self):
        self.words = []
        self.isEnd = False 
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertWord(self, word: str):
        cur = self.root 

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            cur = cur.children[c]
            
            if len(cur.words) < 3:
                cur.words.append(word)
        
        cur.isEnd = True
    
    def getWords(self, word: str):
        cur = self.root
        res = []

        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                res.append(cur.words)
            
            else:
                while len(res) < len(word): # remember to fill in the 
                    res.append([])
                break
        
        return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # trie with an additional property?# the list of words at that point in time?
        products.sort()

        trie = Trie()
        for product in products:
            trie.insertWord(product)
        
        return trie.getWords(searchWord)
