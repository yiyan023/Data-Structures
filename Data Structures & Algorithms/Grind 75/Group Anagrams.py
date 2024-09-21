from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        result = []
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            groups[tuple(count)].append(s)

        result.extend(groups.values())

        return result