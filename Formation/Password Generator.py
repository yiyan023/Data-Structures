def generatePasswords(validCharacters: list[str], minLength: int, maxLength: int) -> list[str]:
    res = []

    def explore(i, arr):
        # cases where it ends: reach end of arr, if max lenght 
        if len(arr) > maxLength:
            return 

        if minLength <= len(arr) <= maxLength:
            res.append(''.join(arr.copy()))
        
        for idx in range(len(validCharacters)):            
            arr.append(validCharacters[idx])
            explore(idx+1, arr)
            arr.pop()
        
    explore(0, [])
    return res

print(generatePasswords(["a","b","c","d"], 0, 0) == [""])
print(generatePasswords(["a","b","c","d"], 0, 1) == ["","a","b","c","d"])
print(generatePasswords(["a","b","c","d"], 1, 1) == ["a","b","c","d"])
print(generatePasswords(["a","b"], 3, 3) == ["aaa","aab","aba","abb","baa","bab","bba","bbb"])
print(generatePasswords(["a"], 2, 4) == ["aa","aaa","aaaa"])
print(generatePasswords(["a"], 2, 4) == ["aa","aaa","aaaa"])
print(generatePasswords(["a","b","c"], 2, 3) == ["aa","aaa","aab","aac","ab","aba","abb","abc",
  "ac","aca","acb","acc","ba","baa","bab","bac","bb","bba","bbb","bbc",
  "bc","bca","bcb","bcc","ca","caa","cab","cac","cb","cba","cbb","cbc",
  "cc","cca","ccb","ccc"])
print(generatePasswords(["a","b","c","d"], 2, 3) == ["aa","aaa","aab","aac","aad","ab","aba","abb",
  "abc","abd","ac","aca","acb","acc","acd","ad","ada","adb","adc",
  "add","ba","baa","bab","bac","bad","bb","bba","bbb","bbc","bbd",
  "bc","bca","bcb","bcc","bcd","bd","bda","bdb","bdc","bdd","ca",
  "caa","cab","cac","cad","cb","cba","cbb","cbc","cbd","cc","cca",
  "ccb","ccc","ccd","cd","cda","cdb","cdc","cdd","da","daa","dab",
  "dac","dad","db","dba","dbb","dbc","dbd","dc","dca","dcb","dcc",
  "dcd","dd","dda","ddb","ddc","ddd"])

print(len(generatePasswords(["a","b","c","d"], 3, 4)) == 320)
print(len(generatePasswords(["a","b","c","d"], 3, 5)) == 1344)
