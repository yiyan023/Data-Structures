class Solution:
    def reverseWords(self, s: str) -> str: 
        word_list = s.split(" ")[::-1]
        return ' '.join(word for word in word_list if len(word))
