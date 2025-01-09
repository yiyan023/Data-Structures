class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        cur = []
        res = []

        for word in words:
            next_phrase = "".join(cur)
            if len(next_phrase + word) > maxWidth:
                spaces = (maxWidth - len(next_phrase) + 1) // (len(cur) - 1) if (len(cur) - 1) > 0 else (maxWidth - len(next_phrase))
                extras = (maxWidth - len(next_phrase) + 1) % (len(cur) - 1) if (len(cur) - 1) > 0 else 0
                string = ""

                for word2 in cur:
                    string += (word2 + " " * spaces)
                    if extras:
                        string += " "
                        extras -= 1
                
                res.append(string[:maxWidth].rstrip(" ") if len(cur) > 1 else string[:maxWidth])
                cur = [word + " "]
            
            else:
                cur.append(word + " ")
        
        last_word = "".join(cur)
        last_word += " " * (maxWidth - len(last_word))
        res.append(last_word[:maxWidth])
        return res
        
