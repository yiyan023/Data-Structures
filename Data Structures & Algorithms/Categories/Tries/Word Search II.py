class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for word in words:
            trie.insert(word)

        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = set()

        def dfs(r, c, node, word):
            if node.isWord:
                res.add(word)
                node.isWord = False

            temp, board[r][c] = board[r][c], "#"

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in node.children:
                    dfs(nr, nc, node.children[board[nr][nc]], word + board[nr][nc])

            board[r][c] = temp
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie.root.children:
                    dfs(r, c, trie.root.children[board[r][c]], board[r][c])
        
        return list(res)
