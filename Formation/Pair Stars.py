def pairStars(word: str) -> str:

    def explore(i, res):
        if i >= len(word):
            return res
        
        if len(res) > 0 and res[-1] == word[i]:
            return explore(i+1, f"{res}*{word[i]}")
        
        else:
            return explore(i+1, f"{res}{word[i]}")
    
    return explore(0, "")

print(pairStars("hello") == "hel*lo")
print(pairStars("xxyy") == "x*xy*y")
print(pairStars("aaaa") == "a*a*a*a")
print(pairStars("aaab") == "a*a*ab")
print(pairStars("aa") == "a*a")
print(pairStars("a") == "a")
print(pairStars("") == "")
print(pairStars("noadjacent") == "noadjacent")
print(pairStars("abba") == "ab*ba")
print(pairStars("abbba") == "ab*b*ba")
