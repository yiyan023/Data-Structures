class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False
        res = []
        buffer = []

        for line in source:
            i = 0
            while i < len(line):
                if not in_block:
                    if i + 1 < len(line) and line[i] == '/' and line[i + 1] == '/':
                        break  # line comment, ignore rest
                    elif i + 1 < len(line) and line[i] == '/' and line[i + 1] == '*':
                        in_block = True
                        i += 1  # skip '*'
                    else:
                        buffer.append(line[i])
                else:
                    if i + 1 < len(line) and line[i] == '*' and line[i + 1] == '/':
                        in_block = False
                        i += 1  # skip '/'
                i += 1

            if buffer and not in_block:
                res.append("".join(buffer))
                buffer = []

        return res
