class MagicDictionary:

    def __init__(self):
        self.magic_dictionary = defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i, c in enumerate(word):
                changed = word[:i] + "*" + word[i+1:]
                self.magic_dictionary[changed].add(word)

    def search(self, searchWord: str) -> bool:
        for i, c in enumerate(searchWord):
            changed = searchWord[:i] + "*" + searchWord[i+1:]
            
            if changed in self.magic_dictionary and (searchWord not in self.magic_dictionary[changed] or len(self.magic_dictionary[changed]) > 1):
                return True 
        
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
