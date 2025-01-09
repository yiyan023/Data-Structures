class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        text_arr = text.split() # create an array of words 
        synonym_hash = defaultdict(list)
        words = {w for ws in synonyms for w in ws}
        root = { word:word for word in words }
        res = []

        def find(word):
            if word != root[word]:
                root[word] = find(root[word])
            
            return root[word]
        
        def union(w1, w2):
            word1, word2 = find(w1), find(w2)

            if word1 != word2:
                root[word2] = word1
        
        for w1, w2 in synonyms:
            union(w1, w2)
        
        for w in words:
            find(w) # make sure they all share the same "root" word
        
        for key in root.keys():
            synonym_hash[root[key]].append(key)
        
        # print(root)
        # print(synonym_hash)
        
        def dfs(i, string):
            if i >= len(text_arr):
                res.append(string[1:])
                return 
            
            if text_arr[i] in root:
                for syn in synonym_hash[root[text_arr[i]]]:
                    dfs(i + 1, string + " " + syn)
            
            else:
                dfs(i + 1, string + " " + text_arr[i])
        
        dfs(0, "")
        return sorted(res)
