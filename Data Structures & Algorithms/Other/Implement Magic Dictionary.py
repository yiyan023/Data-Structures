class MagicDictionary:
    # if searchWord is in the MagicDictionary
    # if one character is different => different test cases with different letters to make sure the code is versatile
    # if more than one character is difference (3)
    # word in MagicDictionary is "hey" and wordSearch is "heyo"
    # word in MagicDictionary is "heyo" and wordSearch is "hey"

    def __init__(self):
        self.magic_dict = set()
        self.words = set()
        self.word_counter = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.words.add(word)

            for i in range(len(word)):
                cur_word = f"{word[:i]}*{word[i+1:]}"
                self.magic_dict.add(cur_word)
                self.word_counter[cur_word] = 1 + self.word_counter.get(cur_word, 0)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            cur_word = f"{searchWord[:i]}*{searchWord[i+1:]}"

            if cur_word in self.magic_dict and (searchWord not in self.words or self.word_counter[cur_word] > 1):
                return True
        
        return False
