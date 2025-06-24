def is_interleaving(x: str, y: str, s: str) -> bool:
    test = []
    def dfs(string, xi, yi):
        if string == s:
            return True 

        if len(string) >= len(s):
            return False 
        
        xWeave = dfs(string + x[xi], xi+1, yi) if xi < len(x) else False
        yWeave = dfs(string + y[yi], xi, yi + 1) if yi < len(y) else False

        return xWeave or yWeave

    return dfs("", 0, 0)

print(is_interleaving("XXXXX", "YYYYY", "shorter") == False)
print(is_interleaving("X", "Y", "longer") == False)
print(is_interleaving("X", "Y", "XY") == True)
print(is_interleaving("X", "Y", "YX") == True)
print(is_interleaving("X", "Y", "XX") == False)
print(is_interleaving("X", "Y", "YY") == False)
print(is_interleaving("ABC", "D", "ABCD") == True)
print(is_interleaving("ABC", "D", "ABDC") == True)
print(is_interleaving("ABC", "D", "ADBC") == True)
print(is_interleaving("ABC", "D", "DABC") == True)
print(is_interleaving("AABCC", "DBBCA", "AADBBCBCAC") == True)
print(is_interleaving("ABC", "BCD", "BABCCD") == True)
print(is_interleaving("ABC", "BCD", "ABCBCD") == True)
print(is_interleaving("ABC", "BCD", "BCDABC") == True)
print(is_interleaving("ABC", "BCD", "BCABDC") == True)
print(is_interleaving("ABC", "BCD", "BABCDD") == False)
print(is_interleaving("ABC", "BCD", "ABBCCD") == True)
print(is_interleaving("ABC", "BCD", "DCCBBA") == False)
print(is_interleaving("ABC", "BCD", "ABBDCC") == False)
print(is_interleaving("ABC", "BCD", "ACBBCD") == False)
