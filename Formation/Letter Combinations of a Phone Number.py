# duplicates? 
# are we returning unique combinations 
# does the order wereturn matter 
# empty string? 
# no 0 or 1? 

# 1. create a dictionary that maps a number to possible letters & use recursion to populate a result array
# base case: 
# if the length of the result string is equal to the initial number string 
# append it to a result array and return 
# otherwise, iterate through the hash map value string & append a letter to the current string & call the recursive step 

# 2. can do this iteratively, but may require more memory & gets challenging to store

DIGIT_TO_CHR = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

def letter_combinations(digits: str) -> list[str]:
    if not digits:
        return []

    res = []

    def dfs(i, string):
        if i >= len(digits):
            res.append(string)
            return 
        
        for c in DIGIT_TO_CHR[digits[i]]:
            dfs(i + 1, string + c)
        
        return 
    
    dfs(0, "")
    return res

if __name__ == "__main__":
    print(letter_combinations('')==[])
print(sorted(letter_combinations('2')) == ['a','b','c'])
print(sorted(letter_combinations('7')) == ['p','q','r','s'])
res23 = letter_combinations('23')
print('ad' in res23 and len(res23) == 9)
print(len(letter_combinations('222')) == 27)

