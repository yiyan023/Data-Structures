from collections import Counter 

def printNameFreq(names: str) -> str:
    if not names:
        return "Nobody appeared."
    
    names_arr = names.split(", ")
    name_freq = Counter(names_arr)
    res = []

    for name, freq in name_freq.items():
        line = f"{name} appeared {freq} time"
        line += "s." if freq > 1 else "."
        res.append(line)
    
    return "\n".join(res)

print(printNameFreq("") == "Nobody appeared.")

print(printNameFreq("Tony") == "Tony appeared 1 time.")

print(printNameFreq("Tony, Jessica") == 
"Tony appeared 1 time.\n\
Jessica appeared 1 time.")

print(printNameFreq("Tony, Tony, Tony") == "Tony appeared 3 times.")

print(printNameFreq("Tony, Jessica, Paavo, Zoe") == 
"Tony appeared 1 time.\n\
Jessica appeared 1 time.\n\
Paavo appeared 1 time.\n\
Zoe appeared 1 time.")

print(printNameFreq("Tony, Jessica, Paavo, Jessica, Tony, Zoe") == 
"Tony appeared 2 times.\n\
Jessica appeared 2 times.\n\
Paavo appeared 1 time.\n\
Zoe appeared 1 time.")
