from collections import defaultdict

# is it possible to have the same number of occurrences (tie)
# what if we have an empty array, no nominations? what should we return?

def risingTideWinner(nominations: list[str]) -> str:
    counter = defaultdict(int)
    max_nom, max_name = 0, None

    for nom in nominations:
        counter[nom] += 1

        if (counter[nom] > max_nom) or (counter[nom] == max_nom and nom > max_name):
            max_nom = counter[nom]
            max_name = nom 
    
    return max_name

print(risingTideWinner([]) == None)
print(risingTideWinner(["pinky"]) == "pinky")
print(risingTideWinner(["tony", "zoe", "jess", "jono", "paavo"])
 == "zoe")
print(risingTideWinner(["oliver", "pixel", "pinky", "pixel"])
 == "pixel")
print(risingTideWinner(["oliver", "pixel", "pinky", "pixel", "pinky"])
 == "pixel")
print(risingTideWinner(["oliver", "pixel", "pinky", "pinky", "pixel"])
 == "pixel")
