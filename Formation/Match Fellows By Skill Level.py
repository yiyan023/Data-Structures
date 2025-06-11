
'''
Match Fellows by skill level

Given an input dictionary mapping Fellows (as string names) to skill ratings, return true if you're able to pair up Fellows with matching skill ratings with no Fellows leftover.
 

EXAMPLE(S)
skillMap = {"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5}
canMatchFellows(skillMap) == True

skillMap = {"oliver": 3, "pixel": 4, "pinky": 5, "tobey": 5}
canMatchFellows(skillMap) == False
 

FUNCTION SIGNATURE
function canMatchFellows(skillMap) {
def canMatchFellows(skillMap: dict) -> bool:
'''

# empty should return true?
# if odd num, do we pair with next skil llevel? or only the same? 
# case sensitiviyu?
# duplicate names? 

from collections import defaultdict

def canMatchFellows(skillMap: dict) -> bool:
    # store the number of odd frequencies 
    odd = 0
    freq = defaultdict(int)

    for level in skillMap.values():
        freq[level] += 1

        if freq[level] % 2:
            odd += 1
        
        else:
            odd -= 1
    
    return not odd

skillMap = {"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5}
print(canMatchFellows(skillMap) == True)

skillMap = {"oliver": 3, "pixel": 4, "pinky": 5, "tobey": 5}
print(canMatchFellows(skillMap) == False)

skillMap = {"oliver": 3, "pixel": 3, "pinky": 3}
print(canMatchFellows(skillMap) == False)

skillMap = {"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5, "paavo" : 1}
print(canMatchFellows(skillMap) == False)

skillMap = {"oliver": 3, "pixel": 3, "pinky": 3, "tobey": 3}
print(canMatchFellows(skillMap) == True)

print(canMatchFellows({"oliver": 1}) == False)

print(canMatchFellows({}) == True)
