class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
            freq = {}
            remove = "!?,;.'"
            
            for char in remove:
                paragraph = paragraph.replace(char, " ")
                    
            words = paragraph.split()
            maxWord, maxNum = "", 0
            print(words)

            for word in words:
                newWord = word.lower()
                
                if newWord not in banned:
                    freq[newWord] = 1 + freq.get(newWord, 0)

                    if freq[newWord] > maxNum:
                        maxNum = freq[newWord]
                        maxWord = newWord
            
            return maxWord
