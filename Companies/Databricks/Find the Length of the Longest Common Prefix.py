class TrieNode:
    def __init__(self):
        self.isWord = False 
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert_word(self, word):
        cur = self.root 

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            cur = cur.children[c]
        
        cur.isWord = True 
    
    def fetch_prefix_len(self, word):
        cur = self.root
        prefix_len = 0

        for c in word:
            if c not in cur.children:
                break 
            
            prefix_len += 1
            cur = cur.children[c]
        
        return prefix_len
    
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        max_len = 0

        for num in arr1:
            trie.insert_word(str(num))
        
        for num in arr2:
            prefix_len = trie.fetch_prefix_len(str(num))
            max_len = max(max_len, prefix_len)
        
        return max_len
