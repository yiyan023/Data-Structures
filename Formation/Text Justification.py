class Solution:
    def fullJustify(self, words, maxWidth):
        if not words or not maxWidth:
            return 0
        
        cur_len = len(words[0])
        cur_line = [words[0]]
        res = []

        def appendLine():
            if len(cur_line) == 1:
                res.append(cur_line[0] + " " * (maxWidth - len(cur_line[0])))
            
            else:
                line = cur_line[0]
                spaces = ((maxWidth - cur_len) // (len(cur_line) - 1))
                remainder = ((maxWidth - cur_len) % (len(cur_line) - 1))

                for j in range(1, len(cur_line)):
                    word = " " * (spaces + 2 if remainder > 0 else spaces + 1) + cur_line[j]
                    remainder -= 1
                    line += word
                
                res.append(line)

        for i in range(1, len(words)):
            if cur_len + 1 + len(words[i]) > maxWidth:
                appendLine()
                    
                cur_len = len(words[i])
                cur_line = [words[i]]
            
            else:
                cur_len += (1 + len(words[i]))
                cur_line.append(words[i])
        
        res.append(' '.join(cur_line) + " " * (maxWidth - cur_len))
        return res
            
