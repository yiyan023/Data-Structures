from collections import deque 

def findHat(dogs: dict, bestFriend: str):
    seen = set()
    seen.add(bestFriend)

    queue = deque()
    queue.append(bestFriend)

    while queue:
        dog = queue.popleft()

        for neigh in dogs[dog]:
            if neigh == "HAT":
                return dog
            
            elif neigh not in seen:
                seen.add(neigh)
                queue.append(neigh)
    
    return "Couldn't find the hat"

dogs = {
  'Carter': ['Fido', 'Ivy'],
  'Ivy': ["HAT"], # Ivy has seen the hat
  'Loki': ['Snoopy'],
  'Pepper': ['Carter'],
  'Snoopy': ['Pepper'],
  'Fido': []
}
print(findHat(dogs, 'Loki') == 'Ivy')

dogs = {
    'Carter': ['Fido', 'Ivy'],
    'Ivy': ["HAT"], # Ivy has seen the hat
    'Loki': ['Snoopy'],
    'Pepper': ['Carter'],
    'Snoopy': ['Pepper'],
    'Fido': []
}
print(findHat(dogs, 'Loki') == "Ivy")
print(findHat(dogs, 'Snoopy') == "Ivy")
print(findHat(dogs, 'Ivy') == "Ivy")
print(findHat(dogs, 'Fido') == "Couldn't find the hat")

dogs = {
    'Ariel': ['Bork'],
    'Bork': ['Cassie'],
    'Cassie': ['Drex'],
    'Drex': ['Zoe'],
    'Zoe': ["HAT"],
}
print(findHat(dogs, "Ariel") == "Zoe")
print(findHat(dogs, "Bork") == "Zoe")
print(findHat(dogs, "Cassie") == "Zoe")
print(findHat(dogs, "Drex") == "Zoe")
print(findHat(dogs, "Zoe") == "Zoe")

dogs = {
    'Zoe': ['Jono'],
    'Jono': ['Angus'], # dead-end, circular knowledge
    'Angus': ['Jono'], # dead-end, circular knowledge
    'Paavo': ['Zoe', 'Oliver'],
    'Oliver': ["HAT"],
}
print(findHat(dogs, "Paavo") == "Oliver")
print(findHat(dogs, "Oliver") == "Oliver")
print(findHat(dogs, "Zoe") == "Couldn't find the hat")
print(findHat(dogs, "Angus") == "Couldn't find the hat")
print(findHat(dogs, "Jono") == "Couldn't find the hat")

dogs = {
  'Zoe': ['Jono'], # circular knowledge
  'Jono': ['Angus'], # circular knowledge
  'Angus': ['Paavo'], # circular knowledge
  'Paavo': ['Zoe', 'Oliver', 'Angus'], # can lead to circular knowledge
  'Oliver': ["HAT"],
}

print(findHat(dogs, "Paavo") == "Oliver")
print(findHat(dogs, "Oliver") == "Oliver")
print(findHat(dogs, "Zoe") == "Oliver")
print(findHat(dogs, "Angus") == "Oliver")
print(findHat(dogs, "Jono") == "Oliver")
