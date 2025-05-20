# 1. loops are possible? 
# 2. no dogs in dog park possible?
# 3. are all the names unique? 
# 4. invalid inputs? 
# 5. is it guaranteed that all dogs in the dog park will be keys in the dogs hash? 
# 6. is it guaranteed that one of the dogs will see the hat, and it will be stored as "HAT" in all caps? 
# 7. case sensitivity? 

# test cases 
# loops inside (between different dogs)
# a direct chain 

# using a queue to process which dogs we want to ask 
# good way to process level by level to make sure we aren't missing dogs that could have seen the hat 
# also making sure to create a visited set so we don't go in cycles 
# time complexity: O(n)
# space complexity: O(n)

import collections

def findHat(dogs: dict, bestFriend: str) -> str:
    queue = collections.deque([bestFriend])
    visited = set()

    while queue: 
        cur = queue.popleft()
        visited.add(cur)

        for nei in dogs[cur]:
            if nei == "HAT":
                return cur 
            
            elif nei not in visited:
                queue.append(nei)
    
    return "Couldn't find the hat"
            
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
