# explore
# what happens if the substring doesn't exist inside the string 
# empty string?
# are duplicates allowed?
# case sensitive? 

# test cases
# empty string, non-empty substring 
# string < substring 
# substring not inside string, but substring < string 
# substring occurs once in string 
# substring occurs multiple times in a string 

# brainstorm 
# 1. iterative sliding window solution 
# check if the current window spells out the substring, if ti does, take note of both the first and last pointers 
# have two min and max values and then find the distance between them at the end 

# 2. recursive solution: 
# base case(s):
# substring > string: return (0, 0)
# substring = part of string: return (i, j)

# personally, i would prefer the iterative solution 

def strDist(word: str,  sub: str) -> int:
    if len(sub) > len(word): 
        return 0
    
    min_start, max_start = float('inf'), 0

    for i, c in enumerate(word):
        if word[i:i+len(sub)] == sub:
            min_start = min(min_start, i)
            max_start = max(max_start, i + len(sub))
    
    return max(0, max_start - min_start)

if __name__ == "__main__":
    print(strDist("catcowcat", "cat") == 9)
    print(strDist("catcowcat", "cow") == 3)
    print(strDist("cccatcowcatxx", "cat") == 9)
    print(strDist("ooowhwhwooo", "whw") == 5)
    print(strDist("", "a") == 0)
    print(strDist("bsdfjgh", "a") == 0)
    print(strDist("catcowcatcowcat", "cat") == 15)
    print(strDist("aa", "aa") == 2)
    print(strDist("catcowcat", "cat") == 9)
    print(strDist("catcowcat", "cow") == 3)
    print(strDist("cccatcowcatxx", "cat") == 9)
    print(strDist("abccatcowcatcatxyz", "cat") == 12)
    print(strDist("ooowhwhwooo", "whw") == 5)
    print(strDist("xyx", "x") == 3)
    print(strDist("xyx", "y") == 1)
    print(strDist("xyx", "z") == 0)
    print(strDist("z", "z") == 1)
    print(strDist("x", "z") == 0)
    print(strDist("", "z") == 0)
    print(strDist("hiHellohihihi", "hi") == 13)
    print(strDist("hiHellohihihi", "hih") == 5)
    print(strDist("hiHellohihihi", "o") == 1)
    print(strDist("hiHellohihihi", "ll") == 2)
