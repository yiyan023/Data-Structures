from collections import defaultdict

class Solution:

    def groupAnagrams(self, strs):
        result = []
        groups = defaultdict(list)

        for s in strs:
            sort = ''.join(sorted(s)) #just sort the word 
            groups[sort].append(s)
        
        result.extend(groups.values())
        return result
        