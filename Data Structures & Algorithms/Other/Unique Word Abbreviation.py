class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbrevs = defaultdict(set)

        for word in dictionary:
            shortForm = f"{word[0]}{len(word)-2}{word[-1]}"
            self.abbrevs[shortForm].add(word)

    def isUnique(self, word: str) -> bool:
        shortForm = f"{word[0]}{len(word)-2}{word[-1]}"
        word_dict = self.abbrevs[shortForm]
        return not len(word_dict) or word in word_dict and len(word_dict) == 1

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
